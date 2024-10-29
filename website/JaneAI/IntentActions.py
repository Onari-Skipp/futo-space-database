from ..db import dbORM
from ..id_generator import *
from .. import function_pool
from huggingface_hub import InferenceClient
from gradio_client import Client
from ..DateToolKit import *
import random
from typing import Dict, List, TypedDict
import re
from ..id_generator import *

class IntentActions:
    """
    Available actions for Intents made available by NLP
    """
    def __init__(self, UserUniqueID: str, model: str):
        self.init = True
        self.model = model
        self.user: dict = dbORM.get_all("User")[f'{function_pool.isFound("User", "user_unique_id", UserUniqueID)}']
        self.JaneDetails = {
            "Name": "Jane",
            "Date Of Birth": clean_date("2024-10-24"),
            "Product Integrated": random.choice(["FUTO Space", "FSpace", "FSpace App"]),
            "Developers": "FSpace Devs",
            "Current Date": clean_date(function_pool.getDateTime()[0]),
            "Current Time": function_pool.getDateTime()[1],
            "Time Of The Day": function_pool.get_time_of_day(function_pool.getDateTime()[1])
        }
        
    def mapIntentToActions(self, detected_intent:str, user_input:str):
        
        intentToActionsMap: dict = {
            "search_product": self.searchForProducts(search_input=user_input),
            "event_inquiry": self.searchForEvents(search_input=user_input),
            "general_inquiry": self.defaultAction(user_prompt=user_input),
            "time_inquiry": random.choice([self.JaneDetails['Current Time'], f"It's {self.JaneDetails['Current Time']}", f"The time is {self.JaneDetails['Current Time']}"]),
            "date_inquiry": random.choice([self.JaneDetails['Current Date'], f"Today's date is {self.JaneDetails['Current Date']}", f"It's {self.JaneDetails['Current Date']}"]),
            "unknown_intent": self.defaultAction(user_prompt=user_input),
            "greeting": self.greetUser()
        }
        return intentToActionsMap[detected_intent]
    
    def greetUser(self):
        responses = [
            f"Hey {self.user['first_name']}, I'm {self.JaneDetails['Name']} your {self.JaneDetails['Product Integrated']} personal assistant. How can i help you today?",
            f"Hello, {self.user['first_name']}! I'm {self.JaneDetails['Name']}, your go-to {self.JaneDetails['Product Integrated']} personal assistant. What can I do for you?",
            f"Hi {self.user['first_name']}, I'm {self.JaneDetails['Name']}, your dedicated {self.JaneDetails['Product Integrated']} personal assistant. How can I assist you today?",
            f"Good {self.JaneDetails['Time Of The Day']}, {self.user['first_name']}. I am {self.JaneDetails['Name']}, your {self.JaneDetails['Product Integrated']} personal assistant. Please let me know how I can be of service.",
            f"Hello, {self.user['first_name']}. I'm {self.JaneDetails['Name']}, your {self.JaneDetails['Product Integrated']} personal assistant. Is there anything specific you'd like help with today?",
        ]
        return random.choice(responses)
    
    def searchForProducts(self, search_input: str):
        all_products = dbORM.get_all("Products")
        replacement_string = generate_id(8)
        
        search_input = search_input.lower()
        
        matching_product_names: list = []
        matching_product_ids: list = []
        
        # Seacrh Algorithim
        class Product(TypedDict):
            user_id: str
            product_id: str
            name: str
            price: str
            description: str
            category: str
            image_url: str
            quantity: str
            is_stock: str
            id: str

        def search_marketplace(
            products: Dict[str, Product],
            search_query: str,
            *,
            categories: List[str] = None,
            min_price: float = None,
            max_price: float = None,
            in_stock_only: bool = False
        ) -> List[Dict]:
            """
            Search marketplace products with improved matching.
            
            Args:
                products: Dictionary of product data
                search_query: Search terms from user
                categories: Optional list of categories to filter by
                min_price: Optional minimum price filter
                max_price: Optional maximum price filter
                in_stock_only: Optional filter for in-stock items only
            
            Returns:
                List of matching product dictionaries
            """
            # Process search query
            stop_words = {'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 
                        'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 
                        'to', 'was', 'were', 'will', 'with', 'look', 'searching', 'search',
                        'find', 'show', 'me', 'get', 'cheap', 'expensive', 'marketplace'}
            
            # Extract meaningful terms from search query
            search_terms = set()
            query_words = re.findall(r'\w+', search_query.lower())
            
            # Process price indicators in search
            price_indicators = {
                'cheap': lambda p: float(p) < 20000,
                'expensive': lambda p: float(p) > 50000,
                'affordable': lambda p: float(p) < 30000,
            }
            
            price_filter = None
            numeric_prices = []

            for word in query_words:
                if word in price_indicators:
                    price_filter = price_indicators[word]
                elif word not in stop_words:
                    search_terms.add(word)
                
                # Detect numeric prices (e.g., "100", "$100", "under 400")
                match = re.match(r'(\d+)', word)
                if match:
                    numeric_prices.append(float(match.group(1)))
            
            # If a specific price is mentioned, use it for min or max price filtering
            if numeric_prices:
                min_price = min_price or min(numeric_prices)
                max_price = max_price or max(numeric_prices)

            matching_products = []
            
            for product in products.values():
                # Create searchable text from product details
                searchable_text = ' '.join([
                    product['name'].lower(),
                    product['description'].lower(),
                    product['category'].lower()
                ])
                
                # Check for matches (now requires at least one search term to match)
                if search_terms and not any(term in searchable_text for term in search_terms):
                    continue
                
                # Apply category filter
                if categories and product['category'] not in categories:
                    continue
                
                # Apply price filters
                price = float(product['price'])
                if min_price is not None and price < min_price:
                    continue
                if max_price is not None and price > max_price:
                    continue
                if price_filter and not price_filter(price):
                    continue
                
                # Apply stock filter
                if in_stock_only and (
                    product['is_stock'].lower() != 'true' or 
                    int(product['quantity']) <= 0
                ):
                    continue

                matching_products.append(product)
            
            # Sort by relevance and price
            if 'cheap' in query_words:
                # Sort by lowest prices (ascending)
                matching_products.sort(key=lambda p: float(p['price']))
            elif 'expensive' in query_words:
                # Sort by highest prices (descending)
                matching_products.sort(key=lambda p: -float(p['price']))
            else:
                # Default: sort by relevance and then by descending price
                matching_products.sort(
                    key=lambda p: (_calculate_relevance(p, search_terms), -float(p['price'])),
                    reverse=True
                )
            
            # If "cheap" or "expensive" is detected, return the top two results.
            if 'cheap' in query_words:
                matching_products = matching_products[:2]
            elif 'expensive' in query_words:
                matching_products = matching_products[:2]
            
            return matching_products

        def _calculate_relevance(product: Product, search_terms: set) -> float:
            """
            Calculate relevance score for a product with improved weighting.
            """
            if not search_terms:
                return 1.0
            
            score = 0.0
            
            # Search in different fields with weights
            fields = {
                'name': 3.0,
                'category': 2.0,
                'description': 1.0
            }
            
            for term in search_terms:
                for field, weight in fields.items():
                    field_text = product[field].lower()
                    # Exact word match gets more points
                    if f' {term} ' in f' {field_text} ':
                        score += 2.0 * weight
                    # Partial match gets fewer points
                    elif term in field_text:
                        score += 1.0 * weight
            
            return score
        
        results = search_marketplace(all_products, search_input)
        matching_product_names = [p['name'] for p in results]
        matching_product_ids = [p['product_id'] for p in results]
        
        
        if len(matching_product_ids) == 0:
            response: str = random.choice([
                f"Sorry {self.user['first_name']}, I couldn't find any products that match your preferences. Please try again!",
                f"Unfortunately, I wasn't able to find any products for you. Would you like to search for something else?",
                f"I couldn't locate any products that fit your criteria. Maybe you want to adjust your search?",
                f"Looks like there are no products that match your request. Feel free to ask about something else!"
            ])
            generated_links: list = []
            
        else:
            response: str = random.choice([
                f"{self.user['first_name']}, check these out! I found some great products that match your preferences. {replacement_string}\n What do you think?",
                f"take a look at these cool products I found! {replacement_string}",
                f"I think you might like these products. {replacement_string} Check them out!",
                f"I've identified these products {replacement_string}"
            ])
            products_names_listed: str = function_pool.list_to_string(matching_product_names) if len(matching_product_names) != 0 else ""
            response: str = response.replace(replacement_string, products_names_listed)
            
            generated_links: list = []
            if len(matching_product_ids) != 0:
                for _id in matching_product_ids:
                    product_link: str = f"https://futo-space.vercel.app/dashboard/skippsdavid/marketplace/product/{_id}"
                    generated_links.append(product_link)
        
        return [response, matching_product_ids, "Product", generated_links]

    
    def searchForEvents(self, search_input: str):
        return "Search Products"
    
    def defaultAction(self, user_prompt: str):
        model = self.model
        if model == "base":
            client = InferenceClient(api_key="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")
    
            response_list = []

            # for message in client.chat_completion(
            #     model="microsoft/Phi-3.5-mini-instruct",
            #     messages=[{"role": "user", "content": user_prompt}],
            #     max_tokens=500,
            #     stream=True,
            # ):
            #     generated_text = message.choices[0].delta.content
            #     response_list.append(generated_text)
            
        
            messages = [
	            { "role": "user", "content": user_prompt }
            ]

            stream = client.chat.completions.create(
                # model="microsoft/Phi-3.5-mini-instruct", 
                model="mistralai/Mistral-7B-Instruct-v0.3", 
                messages=messages, 
                max_tokens=500,
                stream=True
            )

            for chunk in stream:
                response_list.append(chunk.choices[0].delta.content)
                
            return {"prompt": user_prompt, "model": model, "response": " ".join(response_list)}
            
        elif model == "Jane-Fine-Tuned":
            client = Client("FSpaceDev/FSpace-Jane-AI")
            result = client.predict(
                    message=user_prompt,
                    system_message="You are a friendly Chatbot.",
                    max_tokens=512,
                    temperature=0.7,
                    top_p=0.95,
                    api_name="/chat"
            )
            print(result)
            fine_tuned_response = result
            return {"prompt": user_prompt, "model": model, "response": fine_tuned_response}
        else:
            return {"prompt": user_prompt, "model": model, "response": "No Model Chosen"}
        
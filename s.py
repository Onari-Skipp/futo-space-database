# w = {"0": {"id": "0", "email": "", "password": "", "name": "", "age": "", "description": "", "userType": "", "niche": "", "username": ""}, "1": {"name": "Helen Paul"}}
# c = "name"
# it = "Helen Paul"
# i = f"{c} -> {it}"

# def find():
# 	for k, v in w.items():
# 		# print(f"{k} -> {v}")

# 		for ks, vs in v.items():
# 			search_model = f"{ks} -> {vs}"
# 			# print(f"{k}. {ks} -> {vs}")
# 			if i == search_model:
# 				return [k, ks]
			

# print(find())

# import requests
# url = "https://wrldoc.vercel.app"
# response = requests.get(url)

# print(f'Status Code: {response.status_code}')
# print('Response Content:')
# print(response.text)
# Status Code: 200
# Response Content:
# <!DOCTYPE html>
# <html>
# <head>
# 	<meta charset="utf-8">
# 	<meta name="viewport" content="width=device-width, initial-scale=1">
# 	<title>WRLD - We Really Love Developing</title>
# 	<link rel="stylesheet" type="text/css" href="stylesheet.css">
# 	<link rel="icon" href="static/WRLD-icon.png">
# </head>
# <body>
# 	<header>
# 		<img src="static/WRLD-icon.png" alt="Logo">

# 		<nav>
# 			<a href="#" class="nav-menu active">Home</a>
# 			<a href="#getstarted" class="nav-menu">Getting Started</a>
# 			<!-- <a target="_blank" href="#" class="nav-menu">Live Transpiler</a> -->
# 			<a href="#download" class="nav-menu">Download</a>
# 		</nav>
# 	</header>

# 	<main style="display: grid; place-items: center;">
# 		<section id="home">
# 			<!-- Home -->
# 			<div class="hm-left">
# 				<h3>WRLD - We Really Love Developing</h3>
# 				<p><b>WRLD</b> is an evolving, user-friendly tool designed for effortless creation, building, and testing of static webpages/sites. Empowered by its advanced CSS Preprocessor, Lolo, WRLD simplifies the development process, taking care of the intricate details. With WRLD, your focus remains on creative endeavors without the need to worry about the minutiae.</p>

# 				<div class="hm-buttons">
# 					<button title="Read the docs" id="hm-button-wide"><a target="_blank" href="#getstarted" style="color: white; text-decoration: none;">Get started</a></button>
# 					<button title="Download WRLD Tool" style="background : rgba(255, 255, 255, 0.1); border: 2px solid rgba(255, 255, 255, 0.5);"><a target="_blank" href="#download" style="color: white; text-decoration: none;">Download</a></button><!--↓-->
# 				</div>
# 			</div>
# 			<div class="hm-right">
# 				<img src="static/Vertical-wrld.png">
# 			</div>
# 		</section>

# 		<section id="getstarted" style="width: 80%; margin-top: 20px;  display: grid; place-items: center; background: transparent;">
# 			<!-- Getting started -->
# 			<h2 style="text-decoration: underline;">You've heard and seen it...but what does it do?</h2>
# 			<!-- <br> -->
# 			<p>&nbsp;&nbsp;&nbsp;&nbsp;WRLD is a simple, lightweight and useful <i>Tool</i>(<i>still in progress</i>) that's used to create, build and test static webpages/sites. It comes with it's own state-of-the-art <i>Super</i> CSS Preprocessor - <b title="Super Python CSS Preprocessor - Lolo"><a target="_blank" href="pages/docs/getting-started.html#whatislolo" style="color: #a04ea9;">Lolo</a></b>. WRLD is always going to do the heavy lifting so all you have to do create with out sweating the small things.</p>
# 			<br>
# 			<br>
# 			<p>&nbsp;&nbsp;&nbsp;&nbsp;First <a target="_blank" href="#download" style="color: #a04ea9;">Download</a> and Install <b>WRLD</b>, afterwards, open up your preferred <code class="special-key">terminal</code> then throw in the following command to vet weather the installation was successful</p>

# 			<span class="code-command">
# 				wrld -v
# 			</span>

# 			<p>then open up a folder where you'll like your project to live, reopen a <code class="special-key">terminal</code> there then throw this to create a new project:</p>

# 			<span class="code-command">
# 				wrld create-project your-project-name
# 			</span>

# 			<p>replace <code class="special-key">your-project-name</code> with your intended project name...duh 🙄</p>
# 			<br>
# 			<p>&nbsp;&nbsp;&nbsp;&nbsp;Now it's time to build that sucker, building essentially means transpiling your custom files i.e. the ones not supported by browsers e.g. Lolo files(.lolo) to browser readable CSS. Additionally, you could run your webpage on a server(the local one 😂) to testrun the look and feel of your site. And yeah, WRLD does <i>hot reload</i> 🔥 😎.</p>

# 			<p>To do this, simply throw in the following command to just build your Lolo files <mark>without</mark> running it on a server</p>

# 			<span class="code-command">
# 				wrld smart-build your-project-dir
# 			</span>

# 			<p><code class="special-key">smart-build</code> basically just transpiles all your <code class="special-key">.lolo</code> files in your <code class="special-key">project-dir</code> to browser readable <code class="special-text">.css</code>. To build your files and run your webpage locally, throw this command:</p>

# 			<span class="code-command">
# 				wrld serve-project your-project-name
# 			</span>

# 			<p>Violla 🎉 with just two commands, you've created your Webpage. But that's not all friend, see the full docs <a target="_blank" href="pages/docs/getting-started.html" style="color: #a04ea9;">here</a> 🙂</p>
# 		</section>

# 		<section id="download" style="width: 80%; margin-top: 20px;  display: grid; place-items: center; background: transparent;">
# 			<h2>Read the mini documentation? Download the WRLD Tool</h2>
# 			<p>The WRLD Tool offers a convinent way to create, build and manage WRLD Projects. It's flexible meaning it ships bundles with varieties of <a target="_blank" href="pages/docs/getting-started.html#subtools" style="color: #a04ea9;">sub-helpful tools</a>. Happy Developings </p>

# 			<br>
# 			<!-- BETA RELEASES -->
# 			<h4>BEta releases:</h4>
# 			<!-- <button>Download Version Beta 1.0.0</button> -->
# 			<span>None for now!</span>

# 			<hr width="30%">


# 			<!-- STABLE RELEASES -->
# 			<h4>Stable releases:</h4>
# 			<button style="background : rgba(255, 255, 255, 0.1); border: 2px solid rgba(255, 255, 255, 0.5);"><a download="#" style="color: white;">Download Version 1.0.0</a></button>
# 		</section>
# 	</main>

# 	<footer style="display: grid; place-items: center;">
# 		<p>© 2024 David Nzube • <a target="_blank" href="https://github.com/DavidNzube101" style="color: #a04ea9;">Github</a> • <a target="_blank" href="https://twitter.com/DavidNzubee" style="color: #a04ea9;">X (Formerly Twitter)</a> • Built with <b style="background: var(--thmfg); color: var(--thmbg); padding: 5px; border-radius: 1pc;">Lolo (Forest Theme)</b></p>
# 	</footer>

# <script type="text/javascript">
# 	document.addEventListener("DOMContentLoaded", function () {
# 	    const links = document.querySelectorAll('a[href^="#"]');
# 	    for (const link of links) {
# 	        link.addEventListener("click", function (e) {
# 	            e.preventDefault();
# 	            const targetId = this.getAttribute("href").substring(1);
# 	            const targetSection = document.getElementById(targetId);
# 	            window.scrollTo({
# 	                top: targetSection.offsetTop - 50, // Adjust for header height
# 	                behavior: "smooth",
# 	            });
# 	        });
# 	    }
# 	});
# </script>
# </body>
# </html>
# [Finished in 10.2s]

# def add_relationship(self, model_this, model_to, relationship_name):
#     model_this_name = model_this[0]
#     model_to_name = model_to[0]

#     # Validate models
#     if model_this_name not in self.database or model_to_name not in self.database:
#         return f"Invalid models: {model_this_name}, {model_to_name}"

#     # Fetch data
#     data_this = self.database[model_this_name]
#     data_to = self.database[model_to_name]

#     # Identify relationship logic
#     # For example, let's assume model_this has a field 'related_model_id'
#     for key_this, record_this in data_this.items():
#         # Create a relationship by adding 'related_model_id' to each record in model_this
#         record_this[relationship_name] = "related_id"  # Modify this based on your actual relationship logic

#     # Commit changes
#     self.commit([model_this_name, data_this])
#     self.commit([model_to_name, data_to])

#     return f"Relationship '{relationship_name}' added between '{model_this_name}' and '{model_to_name}'"



# db = {
# 	"0": {
# 	    "id": "0",
# 	    "niche": "NULL",
# 	    "email": "NULL",
# 	    "password": "NULL",
# 	    "name": "NULL",
# 	    "age": "NULL",
# 	    "description": "NULL",
# 	    "userType": "NULL",
# 	    "username": "NULL",
# 	    "intrests": "NULL",
# 	    "store_link": "NULL",
# 	    "is_verified_account": "NULL",
# 	    "identification_document": "NULL",
# 	    "identification_document_path": "NULL",
# 	    "profileViewCount": "NULL"
# 	}
# }

# new_user = {'email': "jason@gmail.com", 'name': "Jason", 'password': "abcd23", 'age': "20", 'description': "soccer10", 'niche': "electronics", 'username': "@jason49", 'store_link': "jsn", 'is_verified_account': "False", 'profileViewCount': '0'}
# def add_e(cvp):
# 	for key, value in db.items():
# 		key_ = int(key)

# 	# db[f'{key_ + 1}'] = {}
# 	# db[f'{key_ + 1}']['id'] = f"{key_ + 1}"

# 	# db[f'{key_ + 1}'][f'{col}'] = "NULL"
# 	# db[f'{key_ + 1}'][f'{column}'] = item

# 	db[f'{key_ + 1}'] = {}

# 	get_schema = ['id', 'email', 'password', 'name', 'age', 'description', 'userType', 'niche', 'username', 'intrests', 'store_link', 'is_verified_account', 'identification_document', 'identification_document_path', 'profileViewCount']

# 	print(len(cvp), len(get_schema))

# 	_q = {}
# 	_q["id"] = f"{key_ + 1}"

	
# 	# for col in get_schema:
# 	for k, v in cvp.items():
# 		for col in get_schema:
# 			# print(col, k, v)
# 			if k == col:
# 				_q[f'{k}'] = v
# 			# else:
# 			# 	break
# 			# 	_q[f'{k}'] = "NULL"

# 	k_temp = []
# 	_qr = _q
# 	for k, v in _q.items():
# 		k_temp.append(k)
	
# 	for col in get_schema:
# 		# print(col)
# 		if col in k_temp:
# 			pass
# 		else:
# 			_q[f'{col}'] = "NULL"
# 	# print(col_s)

# 	# for k, v in _q.items():
# 	# 	db[f'{key_ + 1}'][f'{k}'] = f"{v}"
# 	# 	# break

# 	# db[f'{key_ + 1}']['id'] = f"{key_ + 1}"
# 	print(_q)
# 	return db




# s2 = add_e(cvp=new_user)
# print(str(s2).replace("'", '"'))



# e = {
#     "0": {
#         "id": "0",
#         "name": "NULL",
#         "description": "NULL",
#         "price": "NULL",
#         "discount": "NULL",
#         "niche": "NULL",
#         "newPrice": "NULL",
#         "viewCount": "NULL",
#         "image": "NULL",
#         "image_path": "NULL",
#         "user_id": "NULL",
#         "store_id": "NULL",
#         "condition": "NULL"
#     }
# }

# # if n ==


# pr = {
#     "1": {
#         "id": "1",
#         "name": "Three Pair Jean",
#         "description": "LV Three Pair Jean",
#         "price": "56",
#         "discount": "10",
#         "niche": "clothing",
#         "condition": "New",
#         "image": "banner-2.jpg",
#         "image_path": "C:/VidBuy/website/static/_UM_/banner-2.jpg",
#         "user_id": "3",
#         "newPrice": "50.4",
#         "viewCount": "0",
#         "store_id": "1"
#     },
#     "2": {
#         "id": "2",
#         "name": "Blue Water Jug",
#         "description": "Blue Water Jug",
#         "price": "12",
#         "discount": "",
#         "niche": "home_and_kitchen",
#         "condition": "New",
#         "image": "17049610870291928638567209140375.jpg",
#         "image_path": "C:/VidBuy/website/static/_UM_/17049610870291928638567209140375.jpg",
#         "user_id": "4",
#         "newPrice": "12.0",
#         "viewCount": "0",
#         "store_id": "2"
#     },
#     "3": {
#         "id": "3",
#         "name": "Black Versace II",
#         "description": "Black Versace branded kicks. Release II",
#         "price": "110",
#         "discount": "",
#         "niche": "clothing",
#         "condition": "New",
#         "image": "c7fe89774c7d49629709a78a32597349.jpg",
#         "image_path": "C:/VidBuy/website/static/_UM_/c7fe89774c7d49629709a78a32597349.jpg",
#         "user_id": "4",
#         "newPrice": "110.0",
#         "viewCount": "0",
#         "store_id": "2"
#     }
# }

# def goa(c, i):
#     _ = []
#     for k, v in pr.items():
#         for vs in v:
#             if vs == c:
#                 if (pr[f"{k}"][f"{vs}"]) == str(i):
#                     _.append(pr[f'{k}'])

#     return _
# e = (goa(c="user_id", i=4))
# for xs in e:
#     print(f"e-> {xs['id']}")













# w = [{'id': '2', 'name': 'Blue Water Jug', 'description': 'Blue Water Jug', 'price': '12', 'discount': '', 'niche': 'home_and_kitchen', 'condition': 'New', 'image': '17049610870291928638567209140375.jpg', 'image_path': 'C:/VidBuy/website/static/_UM_/17049610870291928638567209140375.jpg', 'user_id': '4', 'newPrice': '12.0', 'viewCount': '0', 'store_id': '2', 'username': '@davidcallium'}, {'id': '3', 'name': 'Black Versace II', 'description': 'Black Versace branded kicks. Release II', 'price': '110', 'discount': '', 'niche': 'clothing', 'condition': 'New', 'image': 'c7fe89774c7d49629709a78a32597349.jpg', 'image_path': 'C:/VidBuy/website/static/_UM_/c7fe89774c7d49629709a78a32597349.jpg', 'user_id': '4', 'newPrice': '110.0', 'viewCount': '0', 'store_id': '2', 'username': '@davidcallium'}, {'id': '4', 'name': 'NW Kicks', 'description': 'cool NW Kicks', 'price': '120', 'discount': '10', 'niche': 'clothing', 'condition': 'New', 'image': '67bb0e041515487fb0eaf2342e813bc3.jpg', 'image_path': 'C:/VidBuy/website/static/_UM_/67bb0e041515487fb0eaf2342e813bc3.jpg', 'user_id': '4', 'newPrice': '108.0', 'viewCount': '0', 'store_id': '2', 'username': '@davidcallium'}, {'id': '5', 'name': 'Yellow-Gold Bracelet', 'description': 'diamond design gold bracelet', 'price': '45', 'discount': '2', 'niche': 'jewelry', 'condition': 'New', 'image': 'Yellow-Gold-Bangle-with-Diamonds_1800x1800.jpg', 'image_path': 'C:/VidBuy/website/static/_UM_/Yellow-Gold-Bangle-with-Diamonds_1800x1800.jpg', 'user_id': '4', 'newPrice': '44.1', 'viewCount': '0', 'store_id': '2', 'username': '@davidcallium'}, {'id': '7', 'name': "Rainbow 'Quinn' Necklace", 'description': "rainbow colored necklace with text 'Quinn'", 'price': '23', 'discount': '', 'niche': 'jewelry', 'condition': 'New', 'image': 'rainbownecklace18kgoldplated.jpg', 'image_path': 'C:/VidBuy/website/static/_UM_/rainbownecklace18kgoldplated.jpg', 'user_id': '4', 'newPrice': '23.0', 'viewCount': '0', 'store_id': '2', 'username': '@davidcallium'}]



# for ws in w:
#     # print(f"this-> {ws}")
#     # for wss, wsv in ws.items():
#     print(f"this-> {ws['name']}")

    # break
# n = {
#         "tw": "action"
#     }
# col = "2"
# w = {
#         "1": {
#             "e": "r", 
#             "wt": "pxs"
#         },
#         "2": {
#             "er": "p",
#             "tw": "kkr"
#         }
#     }
# _q = {}
# for k, v in w.items():
#     for kn, vn in n.items():
#         w[col][kn] = vn

# print(w)


# e = [1, 1, 3, 3, 4, 5]
# print(list(set(e)))












products = {
    "1": {
        "id": "1",
        "name": "Three Pair Jean",
        "description": "LV Three Pair Jean",
        "price": "56",
        "discount": "10",
        "niche": "clothing",
        "condition": "New",
        "image": "banner-2.jpg",
        "image_path": "C:/VidBuy/website/static/_UM_/banner-2.jpg",
        "user_id": "3",
        "newPrice": "50.4",
        "viewCount": "23",
        "store_id": "1",
        "username": "@kirakosarin",
        "is_sponsored": "False"
    },
    "3": {
        "id": "3",
        "name": "Black Versace II",
        "description": "Black Versace branded kicks. Release II",
        "price": "110",
        "discount": "",
        "niche": "clothing",
        "condition": "New",
        "image": "c7fe89774c7d49629709a78a32597349.jpg",
        "image_path": "C:/VidBuy/website/static/_UM_/c7fe89774c7d49629709a78a32597349.jpg",
        "user_id": "4",
        "newPrice": "110.0",
        "viewCount": "19",
        "store_id": "2",
        "username": "@davidcallium",
        "is_sponsored": "False"
    },
    "4": {
        "id": "4",
        "name": "NW Kicks",
        "description": "cool NW Kicks",
        "price": "120",
        "discount": "10",
        "niche": "clothing",
        "condition": "New",
        "image": "67bb0e041515487fb0eaf2342e813bc3.jpg",
        "image_path": "C:/VidBuy/website/static/_UM_/67bb0e041515487fb0eaf2342e813bc3.jpg",
        "user_id": "4",
        "newPrice": "108.0",
        "viewCount": "19",
        "store_id": "2",
        "username": "@davidcallium",
        "is_sponsored": "False"
    },
    "5": {
        "id": "5",
        "name": "Yellow-Gold Bracelet",
        "description": "diamond design gold bracelet",
        "price": "45",
        "discount": "2",
        "niche": "jewelry",
        "condition": "New",
        "image": "Yellow-Gold-Bangle-with-Diamonds_1800x1800.jpg",
        "image_path": "C:/VidBuy/website/static/_UM_/Yellow-Gold-Bangle-with-Diamonds_1800x1800.jpg",
        "user_id": "4",
        "newPrice": "44.1",
        "viewCount": "16",
        "store_id": "2",
        "username": "@davidcallium",
        "is_sponsored": "False"
    },
    "6": {
        "id": "6",
        "name": "Air Jordan Kicks",
        "description": "Purple stripped Black Nike Kicks",
        "price": "96.9",
        "discount": "",
        "niche": "clothing",
        "condition": "New",
        "image": "Default-Vidbuy.png",
        "image_path": "C:/static/_UM_/Default-Vidbuy.png",
        "user_id": "3",
        "newPrice": "96.9",
        "viewCount": "13",
        "store_id": "1",
        "username": "@kirakosarin",
        "is_sponsored": "False"
    },
    "7": {
        "id": "7",
        "name": "Rainbow Quinn Necklace",
        "description": "rainbow colored necklace with text Quinn",
        "price": "23",
        "discount": "",
        "niche": "jewelry",
        "condition": "New",
        "image": "rainbownecklace18kgoldplated.jpg",
        "image_path": "C:/VidBuy/website/static/_UM_/rainbownecklace18kgoldplated.jpg",
        "user_id": "4",
        "newPrice": "23.0",
        "viewCount": "12",
        "store_id": "2",
        "username": "@davidcallium",
        "is_sponsored": "False"
    },
    "8": {
        "id": "8",
        "name": "BYBIT Coins",
        "description": "BYBIT Coins, 20% off",
        "price": "1400",
        "discount": "20",
        "niche": "electronics",
        "condition": "New",
        "image": "BYBIT_LOGO.png",
        "image_path": "C:/VidBuy/website/static/_UM_/BYBIT_LOGO.png",
        "user_id": "4",
        "newPrice": "1120.0",
        "viewCount": "7",
        "store_id": "2",
        "username": "@davidcallium",
        "is_sponsored": "False"
    },
    "9": {
        "id": "9",
        "name": "iPhone 14 Pro Max",
        "description": "iPhone 14 Pro Max - new",
        "price": "1045",
        "discount": "",
        "niche": "electronics",
        "condition": "New",
        "image": "Screenshot_20240209-010050.png",
        "image_path": "C:/VidBuy/website/static/_UM_/Screenshot_20240209-010050.png",
        "user_id": "7",
        "newPrice": "1045.0",
        "viewCount": "5",
        "store_id": "5",
        "username": "@praise",
        "is_sponsored": "True"
    }
}


# def __i(niche):
# 	if (len(products)) == 0:
# 		return None
# 	else:
# 		products_ = []
# 		products_len = []

# 		for k, v in products.items():
# 			products_len.append(k)
			

# 		for n in products_len:
# 			for k, v in products.items():
# 				if niche.lower() == (products[k]['niche']).lower():
# 					products_.append(v)
# 				else:
# 					pass

# 			break

# 		return products_
# # , __i()
# import random
# w = (__i(niche="clothing"))
# random.shuffle(w)
# print(w)


# search_temp_sugg = []
# _ids = []
# _names = []
# _descriptions = []
# _merchants = []
# _niches = []
# _is_sponsored = []

# for k, v in products.items():
#     _ids.append(products[k]['id'])
#     _names.append(products[k]['name'].lower())
#     _descriptions.append(products[k]['description'].lower())
#     _merchants.append(products[k]['username'].lower())
#     _niches.append(products[k]['niche'].lower())
#     _is_sponsored.append(products[k]['is_sponsored'])

#     # print(f"names-> {names}\ndescrip.-> {descriptions}\nusernames-> {merchants}\nniches-> {niches}\n")

# # for merchant1 in _merchants:
# #     for merchant2 in _merchants:
# #         print(merchant1, merchant2)
# #         if merchant1 == merchant2:
# #             _merchants.remove(merchant1)
# #             _merchants.append(merchant2)

# search_temp_sugg.append(f"Ids: {_ids}")
# search_temp_sugg.append(f"Product: {_names}")
# search_temp_sugg.append(f"Descriptions: {_descriptions}")
# search_temp_sugg.append(f"Sellers: {_merchants}")
# search_temp_sugg.append(f"Niches: {_niches}")
# search_temp_sugg.append(f"Sponsored: {_is_sponsored}")

# search_temp = {
#     "id" : _ids,
#     "name" : _names,
#     "description" : _descriptions,
#     "sellers" : _merchants,
#     "niche" : _niches,
#     "is_sponsored": _is_sponsored
# }

# # print(search_temp)

# search_item = 'a'
# length_of_search_item = len(search_item)

# found_ids = []

# for k, v in search_temp.items():
#     for vs in v:
#         if search_item[length_of_search_item - 1] == " ":
#             if search_item in vs:
#                 # print(f"[LOG]: Found `{search_item}` in `{vs}`. KEY: `{k}`. ID: `{v.index(vs)}`. PID: `{search_temp['id'][v.index(vs)]}`")
#                 found_ids.append(search_temp['id'][v.index(vs)])
#         else:
#             search_item_split = search_item.split()
#             if search_item in vs:
#                 # print(f"[LOG]: Found `{search_item}` in `{vs}`. KEY: `{k}`. ID: `{v.index(vs)}`. PID: `{search_temp['id'][v.index(vs)]}`")
#                 found_ids.append(search_temp['id'][v.index(vs)])
#             else:
#                 for word in search_item_split:
#                     if word in vs:
#                         # print(f"[LOG]: Found `{search_item}` in `{vs}`. KEY: `{k}`. ID: `{v.index(vs)}`. PID: `{search_temp['id'][v.index(vs)]}`")
#                         found_ids.append(search_temp['id'][v.index(vs)])
                

# first_found = found_ids[0]
# second_found = found_ids[1]
# # print(products)

# refined = []

# for k in found_ids:
#     if products[k]['is_sponsored'] != "True":
#         pass
#     else:
#         refined.append(products[k])
#         print(True)

# for k in found_ids:
#     refined.append(products[k])

# print(found_ids)
# # print(refined)
# # 

# unique_list = []
# [unique_list.append(x) for x in found_ids if x not in unique_list]
# print(unique_list)



Team = {
    "0": {
        "id": "0",
        "store_id": "NULL",
        "members": "[]",
        "timestamp": "NULL"
    },
    "1": {
        "id": "1",
        "store_id": "5",
        "members": "[3, 4]",
        "timestamp": "24-2-11"
    }
}

Store = {
    "0": {
        "id": "0",
        "name": "NULL",
        "description": "NULL",
        "user_id": "NULL",
        "socials": "NULL"
    },
    "1": {
        "id": "1",
        "name": "KC & A - Kira Clothes and Apparels",
        "description": "One stop shop for Clothes and Apparels. Native, Morden, Semi-Native and more",
        "user_id": "3",
        "socials": "&begin;https://www.facebok.com/kirakosarin442<->https://www.instagram.com/kirakosarin442442<->https://www.wa.me/44232134<->kirakosarin@gmail.com&end;"
    },
    "2": {
        "id": "2",
        "name": "@davidcallium Store",
        "description": "tech bro",
        "user_id": "4",
        "socials": "&begin;https://www.facebook.com/dxpscallium<->https://www.wa.me/0901777<->https://www.instagram.com/@dxpscallium<->davidcalluimpxs@gmail.com&end;"
    },
    "3": {
        "id": "3",
        "name": "@davidnzube00470679 Store",
        "description": "tech",
        "user_id": "5",
        "socials": "&begin;https://www.facebook.com/nzubetech.ng<->https://www.instagram.com/@nzubetech.ng<->https://www.wa.me/23465719999<->david.nzube.official22@gmail.com&end;"
    },
    "4": {
        "id": "4",
        "name": "@pascalneo90186660 Store",
        "description": "",
        "user_id": "6",
        "socials": "[]"
    },
    "5": {
        "id": "5",
        "name": "@praise18083382 Store",
        "description": "Sports bro",
        "user_id": "7",
        "socials": "[]"
    },
    "6": {
        "id": "6",
        "name": "@peace48634337 Store",
        "description": "",
        "user_id": "8",
        "socials": "[]"
    }
}

def is_a_collaborator(id):
    allTeams = []
    for i, j in Team.items():
        allTeams.append(Team[i])

    joined_team = []

    # print(allTeams)

    for i in allTeams:
        for k, v in i.items():
            if int(id) in eval(i['members']):
                joined_team.append(allTeams.index(i))

    duplicates_removed_list = []
    [duplicates_removed_list.append(x) for x in joined_team if x not in duplicates_removed_list]
    _ = []
    for t in duplicates_removed_list:
        _.append(Team[f"{t}"])

    # for q in _:
        # q['name']

    return _

# print(is_a_collaborator("4"))

# c = ""
# v = ""
# print(f"c: {c}\nv: {v}\n-------------------\n")
# rs3 = {"e": "r"}

# for h, i in rs3.items():
#     c = h
#     v = i

# print(f"c: {c}\nv: {v}\n-------------------\n")


vx = {
"NAME": "vidbuy_db",
"PASSWORD": "scrypt:32768:8:1$PmPR6BLpjn7MraZd$b52d4ac7bcd91ba49f5ecda4203475b104fc9cd749bf70e968fbef39c28d95a5e3f5cdf8b3ea0269f765e863850687a7ba260a5e6f598d3ecfb3a3fcc0510fda",
"CONTENT": {
        "Users": [{'0': {'id': 'NULL', 'email': 'NULL', 'password': 'NULL', 'name': 'NULL', 'age': 'NULL', 'description': 'NULL', 'userType': 'NULL', 'niche': 'NULL', 'username': 'NULL', 'intrests': 'NULL', 'store_link': 'NULL', 'is_verified_account': 'NULL', 'identification_document': 'NULL', 'identification_document_path': 'NULL', 'profileViewCount': 'NULL', 'is_pro_user': 'NULL', 'profile_picture': 'NULL', 'user_theme': 'NULL'}}, ['id', 'email', 'password', 'name', 'age', 'description', 'userType', 'niche', 'username', 'intrests', 'store_link', 'is_verified_account', 'identification_document', 'identification_document_path', 'profileViewCount', 'is_pro_user', 'profile_picture', 'user_theme']],
        
        "Notification": [{'0': {'id': 'NULL'}}, ['id']],
        "Product": [{'0': {
                        'id': 'NULL', 
                        'name': 'NULL', 
                        'description': 'NULL', 
                        'price': 'NULL', 
                        'discount': 'NULL', 
                        'niche': 'NULL', 
                        'newPrice': 'NULL', 
                        'viewCount': 'NULL', 
                        'image': 'NULL', 
                        'image_path': 'NULL', 
                        'user_id': 'NULL', 
                        'store_id': 'NULL', 
                        'condition': 'NULL', 
                        'username': 'NULL', 
                        'is_sponsored': 'NULL'}
                    } , ['id', 'name', 'description', 'price', 'discount', 'niche', 'newPrice', 'viewCount', 'image', 'image_path', 'user_id', 'store_id', 'condition', 'username', 'is_sponsored']],

        "Profile_View": [{'0': {
                        'id': 'NULL', 
                        'user_id': 'NULL', 
                        'store_id': 'NULL', 
                        'timestamp': 'NULL'}
                    } , ['id', 'user_id', 'store_id', 'timestamp']],

        "Saved_Product": [{'0': {
                        'id': 'NULL', 
                        'user_id': 'NULL', 
                        'product_id': 'NULL', 
                        'timestamp': 'NULL'}
                    } , ['id', 'user_id', 'product_id', 'timestamp']],

        "Store": [{'0': {
                        'id': 'NULL', 
                        'name': 'NULL', 
                        'description': 'NULL', 
                        'user_id': 'NULL', 
                        'socials': 'NULL', 
                        'banner_picture': 'NULL', 
                        'banner_picture_path': 'NULL', 
                        'address': 'NULL', 
                        'opening_hour': 'NULL', 
                        'closing_hour': 'NULL', 
                        'niche': 'NULL'}
                    } , ['id', 'name', 'description', 'user_id', 'socials', 'banner_picture', 'banner_picture_path', 'address', 'opening_hour', 'closing_hour', 'niche']],

        "Team": [{'0': {
                        'id': 'NULL', 
                        'store_id': 'NULL', 
                        'members': 'NULL', 
                        'timestamp': 'NULL'}
                    } , ['id', 'store_id', 'members', 'timestamp']],

        "View": [{'0': {
                        'id': 'NULL', 
                        'user_id': 'NULL', 
                        'product_id': 'NULL'}
                    } , ['id', 'user_id', 'product_id']]
    }
}

""""""

u = """<h2>Work and Energy in Physics</h2>
<p>The term "work" in science has a definite meaning. Work done in science or in Physics is when a force moves in one point of application along the direction of its line of action. In its simplest mechanical form, it is defined as the product of the force and the distance through which the force acts.</p>

<p><strong>Work = Force x Distance</strong></p>

<p>If the direction of the force and the distance moved are both vertically upwards, we write:</p>
<p><strong>W = F x h</strong> — (1)</p>

<p>If the direction of the force and the distance moved are both horizontal, we write:</p>
<p><strong>W = F x d</strong> — (2)</p>

<h3>Example:</h3>
<p>Find the work done in lifting a mass of 5.0kg through a height of 3.0 meters. Find the work done.</p>
<p><strong>Solution:</strong></p>
<ul>
    <li>m = 5kg</li>
    <li>h = 3m</li>
    <li>F = m x g = 5 x 10 = 50 N</li>
    <li>W = 50 x 3 = 150 Nm</li>
</ul>

<p>In the MKS system of units, work has the absolute unit of kg·m²/s², which is equal to the derived unit of Newton Meter (Nm). In the CGS system of units, the corresponding absolute unit is equal to the dyne centimeter.</p>

<p>In the MKS system of units, 1 Nm is equal to 1 Joule and in the CGS system, 1 dyne centimeter is equal to 1 erg.</p>

<h3>Example:</h3>
<p>A boy weighing 340 N walks up a flight of stairs consisting of 15 steps each of 10 cm high. What work is done by the boy?</p>
<p><strong>Solution:</strong></p>
<ul>
    <li>F = 340N</li>
    <li>h = 10 cm x 15 stairs = 150 cm = 1.5m</li>
    <li>W = F x h = 340 x 1.5 = 510 Nm</li>
</ul>

<h3>Example:</h3>
<p>A boy of mass 70 kg runs up a set of steps of total height 4.0 m. Find the work done.</p>
<p><strong>Solution:</strong></p>
<ul>
    <li>F = m x g = 70 x 10 = 700N</li>
    <li>h = 4m</li>
    <li>W = 700 x 4 = 2800 Nm</li>
</ul>

<h3>Example:</h3>
<p>A loaded sack of total mass 55 kg falls down from the floor of the lorry 3.9 m, calculate the work done.</p>
<p><strong>Solution:</strong></p>
<p>W = 1.93 Nm</p>

<h3>Exercise:</h3>
<p>A boy is pulled 20 m above a horizontal plane with a constant force of n Newton.</p>
<ol>
    <li>Parallel to the plane</li>
    <li>In the direction of angle 60 degrees to the horizontal, calculate the work done.</li>
</ol>

<h2>Energy</h2>
<p>Energy is defined as the capacity to do work.</p>

<h3>Classifications of Mechanical Energy</h3>
<p>Mechanical Energy simply means the energy stored or energy possessed by a virtue of its position or state. The figure below shows a body of mass when the height of h above the suspended. The potential energy possessed by the body is given by:</p>
<p><strong>P.E: F x h</strong></p>

<p>Since the weight of the body is equal to the gravitational force, F is equal to mg, therefore:</p>
<p><strong>P.E = mgh</strong></p>

<h3>Example:</h3>
<p>Find the potential energy of a boy of mass 10 kg standing on a building floor 15 m above the ground.</p>
<p><strong>Solution:</strong></p>
<p>PE = 10 x 10 x 15 = 1500 J</p>

<h3>Kinetic Energy:</h3>
<p>Kinetic energy of a moving body is defined as the ability to do work by the virtue of its motion. If the mass of the body is m, and the body moves with a constant speed v, the kinetic energy is given by:</p>
<p><strong>KE = 1/2 mv²</strong></p>

<h3>Example:</h3>
<p>An object of mass 15 kg is moving with a constant velocity of 15 m/s. Calculate its kinetic energy.</p>
<p><strong>Solution:</strong></p>
<p>KE = 1/2 x 15 x 15² = 112.5 J</p>

<h2>Power</h2>
<p>Power is work done in a given time. It’s the time-rate of doing work. It’s given by:</p>
<p><strong>P = Work Done (Energy Expended) / Time</strong></p>
<p>If work is in Joules and time is in seconds, then the power is measured in J/s (Watts).</p>

<h3>Example:</h3>
<p>A car is moving at 20 m/s. The force retarding its motion is 500 N. Calculate the engine power of the car required to maintain motion.</p>
<p><strong>Solution:</strong></p>
<p>First, calculate the frictional force (F) opposing the motion, which is equal to the force retarding its motion (500 N).</p>
<p>Next, we need to calculate the velocity (v) of the car, which is given as 20 m/s.</p>
<p>We can then calculate the power (P) required to maintain motion using the formula:</p>
<p><strong>P = F × v</strong></p>
<p>Substituting the values, we get:</p>
<p>P = 500 N × 20 m/s = 10,000 W</p>

<h2>Transformation & Conservation of Energy:</h2>
<p>A foregoing discussion has turned that work, potential energy & kinetic energy are all related by a means of simple energy which can be changed from one form to another.</p>

<p>Energy transformation is the process of changing energy from one form to another. This process involves a conversion of energy from one type to another, but the total energy remains constant.</p>

<p>For example, when you turn on a light bulb, electrical energy is converted into light and heat. The energy hasn't been created; it's been transformed from one form (electrical) to another (light and heat).</p>

<p>Energy transformation is an essential concept in physics and is crucial for understanding how energy is harnessed and utilized in various natural and man-made phenomena.</p>

"""

print(repr(u))


# import json
# with open("g.json", "r") as asjska:
#     ewer = json.load(asjska)

# print(ewer)


# e = "<h2>Infinite Geometric Sequence</h2>\n\n<p>Consider the series</p>\n<p>1 + 1/2 + 1/4 + 1/8</p>\n<p>The sum of the first n<sup>th</sup> terms is given by:</p>\n\n<p>S<sub>n</sub> = (a(1 - r<sup>n</sup>))/(1 - r), r < 1\nS<sub>n</sub> = 1(1 - (1/2)<sup>n</sup>)) / (1 - 1/2)\nS<sub>n</sub> = (1 - 1/2<sup>n</sup>) / 1/2\nS<sub>n</sub> = 2(1 - 1/2<sup>n</sup>\nS<sub>n</sub> = (2 - 1/2<sup>(n-1)</sup>)\nas n -> infinity,  then we have:</p>\n\n<p>S<sub>n</sub> -> infinity = lim (2 - 1/2<sup>(n-1)</sup>)\nS<sub>n</sub> -> infinity = 2 - 1/2<sup>∞</sup></p>\n\n<p>If r lies between -1 < r < 1, then r<sup>n</sup> becomes smaller and smaller as n becomes larger and larger. We say that the limiting value of ar<sup>n</sup> as n tends to ∞ is 0. This as n increases, S<sub>n</sub> = approaches a limiting value of a / (1-r).\nWe say that the series converges to the value of a/(1-r) which is the sum to infinite of the series.</p>\n<p>Therefore if -1 < r < 1 i.e. (|r| < 1). The sim to infinite of the geometric series is given by:</p>\n<p>lim<sub>n->∞</sub> = S<sub>n</sub> = a / (1-r)</p>\n \n<p>S<sub>n</sub> = 1 / (1-(1/2)) = 2 / 1 = 2</p>\n\n\n<em><b>Example 1.1</b></em>\n<p>To what sum does the following series:</p>\n<p>1 - 1/3 + 1/9 - 1/27 + …</p>\n<em><b>Solution 1.1</b></em>\n<p>-1 < (1/3) < 1</p>\n<p>S = a/(1-r) = 1 / (1 - (-1/3)) = 3/4</p>\n\n<h3>Mathematical Induction</h3>\n<p>Consider a mathematical statement P(n) associated with each positive integer (that is at all times, n must be positive).\nIf P(1) is true and P(2) is true, then P(k) implies that P(k + 1) os also true. Therefore it says that P(n) is true for all n.</p>\n\n<em><b>Example 1.2</b></em>\n<p>Show that the sum of positive integer 1 + 2 + 3 + … + n = n(n+1)/2</p>\n<em><b>Solution 1.2</b></em>\n<p>First, we check it the statement P(n) is true for n = 1, n = 2</p>\n<p>For n = 1: P(1) = 1, then 1(1+1) / 2 = 2 / 2 = 1</p>\n<p>For n = 2: 1 + 2 = 3, then 2(2+1) / 2 = 3</p>\n\n<p>Next we assume that the statement P(n) is true for n = k that</p>\n<p>1 + 2 + 3 + … K = K(K + 1) / 2 ———(1)</p>\n\n<p>Next, we want to show that P(n) is true for n = k + 1 </p>\n\n<p>From equation (1)</p>\n\n<p>1 + 2 + 3 + … K = (K(K + 1) / 2 ) + (k + 1) </p>\n<p>1 + 2 + 3 + … K = (K(K + 1) + 2(K + 1)) / 2</p>\n<p>1 + 2 + 3 + … K = ((K + 1)[K + 2]) / 2</p>\n\n<p>Therefore, P(n) is true for all n</p>"
# print("<h2>Infinite Geometric Sequence</h2>\n\n<p>Consider the series</p>\n<p>1 + 1/2 + 1/4 + 1/8</p>\n<p>The sum of the first n<sup>th</sup> terms is given by:</p>\n\n<p>S<sub>n</sub> = (a(1 - r<sup>n</sup>))/(1 - r), r < 1\nS<sub>n</sub> = 1(1 - (1/2)<sup>n</sup>)) / (1 - 1/2)\nS<sub>n</sub> = (1 - 1/2<sup>n</sup>) / 1/2\nS<sub>n</sub> = 2(1 - 1/2<sup>n</sup>\nS<sub>n</sub> = (2 - 1/2<sup>(n-1)</sup>)\nas n -> infinity,  then we have:</p>\n\n<p>S<sub>n</sub> -> infinity = lim (2 - 1/2<sup>(n-1)</sup>)\nS<sub>n</sub> -> infinity = 2 - 1/2<sup>∞</sup></p>\n\n<p>If r lies between -1 < r < 1, then r<sup>n</sup> becomes smaller and smaller as n becomes larger and larger. We say that the limiting value of ar<sup>n</sup> as n tends to ∞ is 0. This as n increases, S<sub>n</sub> = approaches a limiting value of a / (1-r).\nWe say that the series converges to the value of a/(1-r) which is the sum to infinite of the series.</p>\n<p>Therefore if -1 < r < 1 i.e. (|r| < 1). The sim to infinite of the geometric series is given by:</p>\n<p>lim<sub>n->∞</sub> = S<sub>n</sub> = a / (1-r)</p>\n \n<p>S<sub>n</sub> = 1 / (1-(1/2)) = 2 / 1 = 2</p>\n\n\n<em><b>Example 1.1</b></em>\n<p>To what sum does the following series:</p>\n<p>1 - 1/3 + 1/9 - 1/27 + …</p>\n<em><b>Solution 1.1</b></em>\n<p>-1 < (1/3) < 1</p>\n<p>S = a/(1-r) = 1 / (1 - (-1/3)) = 3/4</p>\n\n<h3>Mathematical Induction</h3>\n<p>Consider a mathematical statement P(n) associated with each positive integer (that is at all times, n must be positive).\nIf P(1) is true and P(2) is true, then P(k) implies that P(k + 1) os also true. Therefore it says that P(n) is true for all n.</p>\n\n<em><b>Example 1.2</b></em>\n<p>Show that the sum of positive integer 1 + 2 + 3 + … + n = n(n+1)/2</p>\n<em><b>Solution 1.2</b></em>\n<p>First, we check it the statement P(n) is true for n = 1, n = 2</p>\n<p>For n = 1: P(1) = 1, then 1(1+1) / 2 = 2 / 2 = 1</p>\n<p>For n = 2: 1 + 2 = 3, then 2(2+1) / 2 = 3</p>\n\n<p>Next we assume that the statement P(n) is true for n = k that</p>\n<p>1 + 2 + 3 + … K = K(K + 1) / 2 ———(1)</p>\n\n<p>Next, we want to show that P(n) is true for n = k + 1 </p>\n\n<p>From equation (1)</p>\n\n<p>1 + 2 + 3 + … K = (K(K + 1) / 2 ) + (k + 1) </p>\n<p>1 + 2 + 3 + … K = (K(K + 1) + 2(K + 1)) / 2</p>\n<p>1 + 2 + 3 + … K = ((K + 1)[K + 2]) / 2</p>\n\n<p>Therefore, P(n) is true for all n</p>")










amount = 120000
amount = (amount/100)
# amount = "{:.2f}".format(amount)
print((amount))
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


e = [1, 1, 3, 3, 4, 5]
print(list(set(e)))












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
        "viewCount": "20",
        "store_id": "1",
        "username": "@kirakosarin"
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
        "viewCount": "11",
        "store_id": "2",
        "username": "@davidcallium"
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
        "viewCount": "11",
        "store_id": "2",
        "username": "@davidcallium"
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
        "viewCount": "11",
        "store_id": "2",
        "username": "@davidcallium"
    },
    "6": {
        "id": "6",
        "name": "Air Jordan Kicks",
        "description": "Black-Purple themed Nike Air Jordan Kicks",
        "price": "102",
        "discount": "5",
        "niche": "clothing",
        "condition": "New",
        "image": "images_2.jpeg",
        "image_path": "C:/VidBuy/website/static/_UM_/images_2.jpeg",
        "user_id": "3",
        "newPrice": "96.9",
        "viewCount": "3",
        "store_id": "1",
        "username": "@kirakosarin"
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
        "viewCount": "3",
        "store_id": "2",
        "username": "@davidcallium"
    }
}


def __i(niche):
	if (len(products)) == 0:
		return None
	else:
		products_ = []
		products_len = []

		for k, v in products.items():
			products_len.append(k)
			

		for n in products_len:
			for k, v in products.items():
				if niche.lower() == (products[k]['niche']).lower():
					products_.append(v)
				else:
					pass

			break

		return products_
# , __i()
print((__i(niche="clothing")))























# classes.py

class Category:
    def __init__(self, name):
        self.name = name
        self.subcategories = []

class Men(Category):
    def __init__(self):
        super().__init__("Men")
        self.subcategories = ["Shirts", "Pants", "Shoes"]
        self.products = {
            "Shirts": [
                {"id": 1, "name": "Formal Shirt", "price": 799, "image": "mshirt-1.JPEG"},
                {"id": 2, "name": "Formal Shirt", "price": 699, "image": "mshirt-2.JPEG"},
                {"id": 3, "name": "Formal Shirt", "price": 699, "image": "mshirt-3.JPEG"},
                {"id": 4, "name": "Formal Shirt", "price": 699, "image": "mshirt-4.JPEG"},
                {"id": 5, "name": "Formal Shirt", "price": 699, "image": "mshirt-5.JPEG"},
            ],
            "Pants": [
                {"id": 6, "name": "Casual Pant", "price": 899, "image": "mpant-1.JPG"},
                {"id": 7, "name": "Casual Pant", "price": 899, "image": "mpant-2.JPEG"},
                {"id": 8, "name": "Casual Pant", "price": 899, "image": "mpant-3.JPEG"},
                {"id": 9, "name": "Casual Pant", "price": 899, "image": "mpant-4.JPEG"},
                {"id": 10, "name": "Casual Pant", "price": 899, "image": "mpant-5.JPEG"},
            ],
            "Shoes": [
                {"id": 11, "name": "Formal Shoe", "price": 999, "image": "mshoe-1.JPG"},
                {"id": 12, "name": "Running Shoe", "price": 999, "image": "mshoe-2.JPEG"},
                {"id": 13, "name": "Running Shoe", "price": 999, "image": "mshoe-3.JPEG"},
                {"id": 14, "name": "Running Shoe", "price": 999, "image": "mshoe-4.JPEG"},
                {"id": 15, "name": "Formal Shoe", "price": 999, "image": "mshoe-5.JPEG"},
            ]
        }

class Women(Category):
    def __init__(self):
        super().__init__("Women")
        self.subcategories = ["Kurtis", "Dresses", "Handbags"]
        self.products = {
            "Kurtis": [
                {"id": 16, "name": "Floral Kurti", "price": 899, "image": "wkurti-1.JPG"},
                {"id": 17, "name": "Floral Kurti", "price": 999, "image": "wkurti-2.JPEG"},
                {"id": 18, "name": "Floral Kurti", "price": 599, "image": "wkurti-3.JPEG"},
                {"id": 19, "name": "Floral Kurti", "price": 699, "image": "wkurti-4.JPEG"},
                {"id": 20, "name": "Floral Kurti", "price": 899, "image": "wkurti-5.JPEG"},
            ],
            "Dresses": [
                {"id": 21, "name": "Designer Dress", "price": 1099, "image": "wdress-1.JPEG"},
                {"id": 22, "name": "Designer Dress", "price": 899, "image": "wdress-2.JPEG"},
                {"id": 23, "name": "Designer Dress", "price": 9999, "image": "wdress-3.JPEG"},
                {"id": 24, "name": "Designer Dress", "price": 1999, "image": "wdress-4.JPEG"},
                {"id": 25, "name": "Designer Dress", "price": 1000, "image": "wdress-5.JPEG"},

            ],
            "Handbags": [
                {"id": 26, "name": "Designer Handbag", "price": 1099, "image": "whandbag-1.JPG"},
                {"id": 27, "name": "Designer Handbag", "price": 1099, "image": "whandbag-2.JPEG"},
                {"id": 28, "name": "Designer Handbag", "price": 1099, "image": "whandbag-3.JPEG"},
                {"id": 29, "name": "Designer Handbag", "price": 1099, "image": "whandbag-4.JPEG"},
                {"id": 30, "name": "Designer Handbag", "price": 1099, "image": "whandbag-5.JPEG"},

            ]
        }

class Kids(Category):
    def __init__(self):
        super().__init__("Kids")
        self.subcategories = ["T-Shirts", "Shorts", "Shoes"]
        self.products = {
            "T-Shirts": [
                {"id": 31, "name": "Kids T-shirt", "price": 499, "image": "T-shirt-1.JPEG"},
            ],
            "Shorts": [
                {"id": 32, "name": "Kids Shorts", "price": 399, "image": "kshorts-1.JPEG"},
            ],
            "Shoes": [
                {"id": 33, "name": "Kids Shoes", "price": 699, "image": "kshoe-1.JPEG"},
            ]
        }
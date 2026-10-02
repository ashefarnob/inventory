#inventory project
products = [
    {"id": 1, "name": "T-Shirt", "size": "M", "color": "White", "design": "Plain", "gender": "Male", "fabric": "Cotton", "stock": 10},
    {"id": 2, "name": "Polo Shirt", "size": "L", "color": "Black", "design": "Striped", "gender": "Male", "fabric": "Cotton", "stock": 10},
    {"id": 3, "name": "Formal Shirt", "size": "XL", "color": "Blue", "design": "Checked", "gender": "Male", "fabric": "Linen", "stock": 10},
    {"id": 4, "name": "Jeans", "size": "M", "color": "Blue", "design": "Plain", "gender": "Male", "fabric": "Denim", "stock": 10},
    {"id": 5, "name": "Hoodie", "size": "L", "color": "Black", "design": "Printed", "gender": "Male", "fabric": "Cotton", "stock": 10},
    {"id": 6, "name": "Kurti", "size": "M", "color": "Red", "design": "Floral", "gender": "Female", "fabric": "Cotton", "stock": 10},
    {"id": 7, "name": "Saree", "size": "L", "color": "Red", "design": "Embroidered", "gender": "Female", "fabric": "Silk", "stock": 10},
    {"id": 8, "name": "Skirt", "size": "S", "color": "Black", "design": "Plain", "gender": "Female", "fabric": "Synthetic", "stock": 10},
    {"id": 9, "name": "Blouse", "size": "M", "color": "White", "design": "Printed", "gender": "Female", "fabric": "Satin", "stock": 10},
    {"id": 10, "name": "Jacket", "size": "XL", "color": "Brown", "design": "Leather", "gender": "Male", "fabric": "Leather", "stock": 10},
    {"id": 11, "name": "Sweater", "size": "L", "color": "Green", "design": "Patterned", "gender": "Male", "fabric": "Wool", "stock": 10},
    {"id": 12, "name": "Dress", "size": "M", "color": "Pink", "design": "Floral", "gender": "Female", "fabric": "Satin", "stock": 10},
    {"id": 13, "name": "Shorts", "size": "S", "color": "Gray", "design": "Plain", "gender": "Male", "fabric": "Cotton", "stock": 10},
    {"id": 14, "name": "Leggings", "size": "M", "color": "Black", "design": "Plain", "gender": "Female", "fabric": "Synthetic", "stock": 10},
    {"id": 15, "name": "Tank Top", "size": "S", "color": "Yellow", "design": "Printed", "gender": "Female", "fabric": "Cotton", "stock": 10},
    {"id": 16, "name": "Cargo Pants", "size": "XL", "color": "Green", "design": "Pocketed", "gender": "Male", "fabric": "Cotton", "stock": 10},
    {"id": 17, "name": "Long Coat", "size": "L", "color": "Gray", "design": "Plain", "gender": "Female", "fabric": "Wool", "stock": 10},
    {"id": 18, "name": "Sports Jersey", "size": "M", "color": "Blue", "design": "Printed", "gender": "Male", "fabric": "Polyester", "stock": 10},
    {"id": 19, "name": "Party Gown", "size": "L", "color": "Purple", "design": "Embroidered", "gender": "Female", "fabric": "Satin", "stock": 10},
    {"id": 20, "name": "Denim Jacket", "size": "XL", "color": "Blue", "design": "Washed", "gender": "Male", "fabric": "Denim", "stock": 10}]
size=input("Enter a product size")
color=input("Enter a product color")
fabric=input("Enter a product fabric")
gender=input("Enter a product gender")
new_id=int(input("Enter a product id"))

product={
"id":id,
"size":size,
"color":color,
"fabric":fabric,
"gender":gender,
"stock":10

}
products.append(product)
print(products)

delete_id=int(input("Enter the product_id"))
for product in products:
    if product["id"] == delete_id:
     products.remove(product)
     break
print(products)
    


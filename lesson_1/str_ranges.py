# colors = ["red", "green", "blue"]
# for (idx, color) in enumerate(colors):
#     print(f"Color {color} is at index {idx}.")

# print(list(enumerate(colors)))
data = {
    'name': 'Srdjan',
    'city': 'Belgrade',
    'favorite_colors': ['blue', 'purple'],
    }

data.setdefault('country', 'Serbia')
print(data)
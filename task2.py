class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

# Функція для вставки нового вузла в дерево
def insert_node(root, key):
    if root is None:
        return TreeNode(key)

    if key < root.value:
        root.left = insert_node(root.left, key)
    else:
        root.right = insert_node(root.right, key)

    return root

# Функція для знаходження найменшого значення в бінарному дереві пошуку
def find_min_value(root):
    if root is None:
        return None  # Дерево порожнє

    current = root
    while current.left is not None:
        current = current.left

    return current.value

# Тестування функції на прикладі
root = None
keys = [20, 8, 22, 4, 12, 10, 14]

for key in keys:
    root = insert_node(root, key)

print(f"Найменше значення у дереві: {find_min_value(root)}")

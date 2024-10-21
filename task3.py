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

# Функція для знаходження суми всіх значень у дереві
def calculate_tree_sum(root):
    if root is None:
        return 0
    return root.value + calculate_tree_sum(root.left) + calculate_tree_sum(root.right)

# Тестуємо функцію на прикладі
root = None
keys = [20, 8, 22, 4, 12, 10, 14]

for key in keys:
    root = insert_node(root, key)

print(f"Сума всіх значень у дереві: {calculate_tree_sum(root)}")

# 代码生成时间: 2025-09-24 20:41:26
import requests

class InventoryManagement:
    def __init__(self, base_url):
        """
        初始化库存管理系统
        :param base_url: API的基础URL
        """
        self.base_url = base_url

    def get_inventory(self):
        """
        获取库存列表
        :return: 库存列表或错误信息
        """
        try:
            response = requests.get(f"{self.base_url}/inventory")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            return f"HTTP error occurred: {http_err}"
        except Exception as err:
            return f"An error occurred: {err}"

    def add_item(self, item_id, quantity):
        """
        向库存中添加物品
        :param item_id: 物品ID
        :param quantity: 添加的数量
        :return: 添加结果或错误信息
        """
        try:
            response = requests.post(
                f"{self.base_url}/inventory",
                json={"item_id": item_id, "quantity": quantity}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            return f"HTTP error occurred: {http_err}"
        except Exception as err:
            return f"An error occurred: {err}"

    def update_item(self, item_id, quantity):
        """
        更新库存中的物品数量
        :param item_id: 物品ID
        :param quantity: 更新后的数量
        :return: 更新结果或错误信息
        """
        try:
            response = requests.put(
                f"{self.base_url}/inventory/{item_id}",
                json={"quantity": quantity}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            return f"HTTP error occurred: {http_err}"
        except Exception as err:
            return f"An error occurred: {err}"

    def delete_item(self, item_id):
        """
        从库存中删除物品
        :param item_id: 物品ID
        :return: 删除结果或错误信息
        """
        try:
            response = requests.delete(f"{self.base_url}/inventory/{item_id}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            return f"HTTP error occurred: {http_err}"
        except Exception as err:
            return f"An error occurred: {err}"

# 示例用法
if __name__ == "__main__":
    base_url = "http://your-api-url.com"
    inventory_mgmt = InventoryManagement(base_url)

    # 获取库存
    inventory = inventory_mgmt.get_inventory()
    print("Inventory:", inventory)

    # 添加物品
    result = inventory_mgmt.add_item("item123", 10)
    print("Add item result:", result)

    # 更新物品数量
    result = inventory_mgmt.update_item("item123", 15)
    print("Update item result:", result)

    # 删除物品
    result = inventory_mgmt.delete_item("item123")
    print("Delete item result:", result)
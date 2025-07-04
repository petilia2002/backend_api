class ItemNotFound(Exception):
    def __init__(self, item_id: int = None, item_name: str = None):
        self.item_id = item_id
        self.item_name = item_name
        message = f"{item_name if item_name else 'Item'} {f'with ID {item_id}' if item_id else ''} not found"
        super().__init__(message)

class ShoppingListError(Exception):


class ProductNotFoundError(ShoppingListError):


class CategoryNotFoundError(ShoppingListError):


class ValidationError(ShoppingListError):


class StorageError(ShoppingListError):


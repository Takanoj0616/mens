from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """JSON フィールドから特定のキーの値を取得する"""
    if isinstance(dictionary, dict):
        return dictionary.get(key, "予定なし")
    return "予定なし"
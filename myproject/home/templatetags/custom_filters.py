from django import template

register = template.Library()

@register.filter
def currency(value):
    """
    Format số tiền thành kiểu 45.000 đ
    """
    try:
        value = float(value)
        # Định dạng số có dấu chấm ngăn cách hàng nghìn
        formatted = f"{value:,.2f}".replace(",", ".")
        return f"$ {formatted}"
    except (ValueError, TypeError):
        return "$ 0"
"""
f"{value:,.0f}".replace(",", ".")
.0f => làm tròn số thập phân (0 chữ số thập phân)
, => thêm dấu phẩy phân cách hàng nghìn
replace => 4,000,000 => 4.000.000 đ
"""
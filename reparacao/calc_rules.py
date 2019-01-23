from decimal import Decimal

def calc_total(rep):
    total_to_pay = Decimal(rep["price"]) * int(rep["units"]) * int(rep["quantity"]) *Decimal((rep["tax"]+100)/100)
    if rep["discount"] and Decimal(rep["discount"])!=Decimal(0):
        total_to_pay = total_to_pay * Decimal((100-Decimal(rep["discount"]))/100)
    total_to_pay = round(total_to_pay,2)
    return total_to_pay
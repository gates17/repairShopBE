from decimal import Decimal

def calc_total(rep):
    tax = float(rep['tax'])
    tax = Decimal(tax)

    total_to_pay = Decimal(rep["price"]) * int(rep["units"]) * int(rep["quantity"])
    if rep["discount"] and Decimal(rep["discount"]) != Decimal(0):
        total_to_pay = total_to_pay * Decimal((100 - Decimal(rep["discount"])) / 100)

    total_to_pay_with_tax = total_to_pay *Decimal((tax+100)/100)

    tax_to_pay = total_to_pay_with_tax - total_to_pay


    total_to_pay = round(total_to_pay,2)
    total_to_pay_with_tax=round(total_to_pay_with_tax,2)
    tax_to_pay=round(tax_to_pay,2)

    total_dict={'total_to_pay':total_to_pay,'total_to_pay_with_tax':total_to_pay_with_tax,'tax_to_pay':tax_to_pay}
    return total_dict
def calculate_discount(sum: float, per_sale: int) -> float:

    if not ((isinstance(sum, float)) and (isinstance(per_sale, int))):
        raise TypeError(f'Недопустимый(ые) тип(ы) значения(й) {sum} и(или) {per_sale}')
    if sum < 0:
        raise ValueError(f"сумма покупки {sum} не может быть отрицательной")
    if not (0 <= per_sale <= 100):
        raise ValueError(f"Недопустимое значение скидки {per_sale}")
    result = sum * (1 - per_sale / 100)
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(calculate_discount(200.0, 10))

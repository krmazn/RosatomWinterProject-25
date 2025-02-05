def calculate_delta(current_price, predicted_price) -> str:
    delta = float(predicted_price) / float(current_price)
    delta = delta - 1

    if delta >= 0:
        return f"+{100 * float(f'{delta:.2f}')}%"
    return f"{100 * float(f'{delta:.2f}')}%"

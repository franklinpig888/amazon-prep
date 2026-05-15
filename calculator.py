def calculate_tip(bill, tip_percent):
    return bill * (tip_percent / 100)

def split_bill(total, num_people):
    return total / num_people

def main():
    num_people = int(input("How many people are splitting?"))
    amount = float(input("What is the bill amount?"))
    tip_percent = int(input("what percent do you want to tip? 10, 15 or 20"))

    tip_amount = calculate_tip(amount, tip_percent)
    total = amount + tip_amount
    each = split_bill(total, num_people)

    print(f"Bill: ${amount:.2f}")
    print(f"Tip: ${tip_amount:.2f}")
    print(f"Total: ${total:.2f}")
    print(f"Each person pays: ${each:.2f}")

main()
# Workshop Energy Cost Estimator
# Calculates daily and monthly energy (kWh) and cost for workshop machines.
# Own twist: shows which machine uses the most energy and its % share of the bill.

DAYS_IN_MONTH = 30  # assumed number of working days per month


def get_number(prompt, minimum=0, whole=False):
    """Keep asking until the user types a valid number above the minimum.
    Returns an int if whole=True, otherwise a float."""
    while True:
        text = input(prompt)
        try:
            # Convert the typed text to a number
            value = int(text) if whole else float(text)
        except ValueError:
            print("Invalid input. Please type a number, e.g. 5 or 2.5.")
            continue
        if value <= minimum:
            print(f"Please enter a number greater than {minimum}.")
        else:
            return value


def daily_kwh(power_watts, hours_per_day):
    """Convert watts and hours into kilowatt-hours used per day."""
    return (power_watts * hours_per_day) / 1000


def main():
    print("=== Workshop Energy Cost Estimator ===")

    # Ask how many machines there are
    count = get_number("How many machines? ", whole=True)
    tariff = get_number("Enter your tariff (Naira per kWh): ")

    # Lists to store each machine's details
    names = []
    daily_energies = []

    # Loop to collect the data for each machine
    for i in range(1, count + 1):
        print(f"\n--- Machine {i} ---")
        name = input("Name: ").strip()
        if name == "":
            name = f"Machine {i}"  # default name if left blank
        while True:
            power = get_number("Power (watts): ")
            hours = get_number("Hours used per day (max 24): ")
            if hours > 24:
                print("A day has only 24 hours. Try again.")
            else:
                break
        names.append(name)
        daily_energies.append(daily_kwh(power, hours))

    # Totals
    total_daily = sum(daily_energies)
    total_monthly = total_daily * DAYS_IN_MONTH
    daily_cost = total_daily * tariff
    monthly_cost = total_monthly * tariff

    # Results table
    print("\n=== RESULTS ===")
    print(f"{'Machine':<18}{'kWh/day':>10}{'kWh/month':>12}")
    for i in range(count):
        print(f"{names[i]:<18}{daily_energies[i]:>10.2f}{daily_energies[i] * DAYS_IN_MONTH:>12.2f}")
    print("-" * 40)
    print(f"Total daily energy:   {total_daily:.2f} kWh")
    print(f"Total monthly energy: {total_monthly:.2f} kWh ({DAYS_IN_MONTH} days)")
    print(f"Daily cost:           N{daily_cost:,.2f}")
    print(f"Monthly cost:         N{monthly_cost:,.2f}")

    # OWN TWIST: find the biggest energy user and its share of the total
    biggest = max(daily_energies)
    index = daily_energies.index(biggest)
    share = (biggest / total_daily) * 100
    print("\n=== BIGGEST ENERGY USER ===")
    print(f"{names[index]} uses {share:.1f}% of your energy.")
    if share >= 50:
        print("Tip: this machine dominates your bill. Reduce its running hours first.")
    elif share >= 30:
        print("Tip: this machine is a major cost. Check if it can run less.")
    else:
        print("Your energy use is fairly spread across machines.")


main()

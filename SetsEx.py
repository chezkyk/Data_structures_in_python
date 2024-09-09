# Example Input
broker_a_stocks = {"AAPL", "MSFT", "GOOGL", "TSLA", "AMZN"}
broker_b_stocks = {"NFLX", "MSFT", "TSLA", "FB", "AAPL"}


def find_common_stocks(broker_a_stocks, broker_b_stocks):
    # for stock in broker_a_stocks:
    #     if stock in broker_b_stocks:
    #         common_stocks_list.append(stock)
    # return common_stocks_list
    common_stocks_list = list(broker_a_stocks.intersection(broker_b_stocks))
    common_stocks_list.sort(key=None, reverse=False)
    return common_stocks_list


print(find_common_stocks(broker_a_stocks, broker_b_stocks))

print("---" * 100)

def unique_expense_categories(list_of_sets):
    unique_categories = set()
    for stock_set in list_of_sets:
        unique_categories.update(stock_set)
    unique_list =  list(unique_categories)
    unique_list.sort(key=None, reverse=False)
    return unique_list

monthly_expenses = [
    {"Travel", "Marketing", "Salaries"},
    {"Marketing", "R&D", "Utilities"},
    {"Salaries", "Legal", "Marketing"},
    {"IT", "Travel", "R&D"}
]
print(unique_expense_categories(monthly_expenses))

print("---" * 100)

def analyze_frozen_assets(list_of_frozen_sets):
    set_a = set()
    set_b = set()
    set_c = set()
    set_a = set(list_of_frozen_sets[0])
    set_b = set(list_of_frozen_sets[1])
    set_c = set(list_of_frozen_sets[2])
    print(type(set_a), type(set_b), type(set_c))
    all_frozen_assets = set_a.union(set_b, set_c)
    always_frozen_assets = set_a.intersection(set_b, set_c)
    frozen_in_only_one_month = set_a.difference(set_b, set_c)
    frozen_in_only_one_month.update(set_b.difference(set_a, set_c))
    frozen_in_only_one_month.update(set_c.difference(set_a, set_b))
    ans = {"All frozen assets:" : all_frozen_assets, "Always frozen assets:" : always_frozen_assets, "Frozen in only one month:" : frozen_in_only_one_month }
    return ans

monthly_frozen_assets = [
    frozenset({"Asset1", "Asset2", "Asset3"}),
    frozenset({"Asset2", "Asset4", "Asset3"}),
    frozenset({"Asset2", "Asset3", "Asset5"}),
]
print(analyze_frozen_assets(monthly_frozen_assets))


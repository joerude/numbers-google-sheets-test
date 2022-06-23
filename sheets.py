import gspread
from utils import exchange_rate_usdrub_today

sa = gspread.service_account()
sh = sa.open("Тестовое")
# wks = sh.worksheet("Лист1")
wks = sh.worksheet("Лист2")

cnt_cols = len(wks.col_values(1))
print(cnt_cols)

cell_values = list(range(cnt_cols + 1))
print(cell_values)

cell_list = wks.range(f'E2:E{cnt_cols}')

# for i in range(cnt_cols):
#     usd_price = float(wks.acell(f'C{i + 2}').value)
    # cell_list[i].value = usd_price * exchange_rate_usdrub_today()
    # print(i, usd_price, usd_price * exchange_rate_usdrub_today())


# wks.update_cells(cell_list)

print(wks.get_all_values())
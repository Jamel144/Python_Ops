#Make a cubic meter to KWH

is_imperial = input("Do you have an imperial meter? (Y/N) ").upper()

if is_imperial == "Y":
    imperial_unit = int(input("Enter imperial value "))
    calorific_figure = int(input("Enter calorific figure "))


    def imp_to_kwh(imperial_unit, calorific_figure):
        kwh =  imperial_unit * 2.83 * calorific_figure * 1.02264 / 3.6
        return round(kwh)
    print(f"Your read is {imp_to_kwh(imperial_unit, calorific_figure)}KWH")

elif is_imperial == "N":
    cubic_meter = int(input("Enter cubic meter value "))
    calorific_figure = int(input("Enter calorific figure "))
             
    def m3_to_kwh(cubic_meter, calorific_figure):
        kwh =  cubic_meter * calorific_figure * 1.02264 / 3.6
        return round(kwh)
    print(f"Your read is {m3_to_kwh(cubic_meter, calorific_figure)}KWH")

else:
    print("Please eneter 'Y' or 'N'")


# First program works! :) 


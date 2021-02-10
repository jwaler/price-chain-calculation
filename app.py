import datetime
container = 9
insurance = 0.005
x = datetime.datetime.now()

# symbol, fob, cif, custom tax, vat, currency rate, currency symbol, pallet price
logcost = [
    ('Taiwan', 960, 3740, 0.1, 0.05, 45, 'TWD', 12000),
    ('Hong Kong', 960, 3740, 0, 0, 9.5, 'HKD', 3750),
    ('Japan', 960, 3740, 0.34, 0.08, 126, 'YEN', 75000),
    ('Singapore', 960, 3740, 0, 0, 1.7, 'SGD', 750),
    ('Australia', 960, 3740, 0.05, 0.10, 1.56, 'AUD', 600),
    ('New Zealand', 960, 3740, 0.2, 0.10, 126, 'NZD', 600),
    ('China', 960, 3740, 0.20, 0.05, 7, 'RMB', 3500),
    ('Philippines', 960, 3740, 0.20, 0.05, 58, 'Pesos', 29000),
    ('South Korea', 960, 3740, 0.08, 0.10, 1.3, 'k WON', 400),  # K Won
    ('Malaysia', 960, 3740, 0.20, 0.05, 4.91, 'MYR', 1473)
]

# name, PC, pc/case, case/pal
produit = [
    ('VEGAN CHOCO CAKE', 20.56, 36, 250),
    ('CHEESECAKE CLASSIC', 10.39, 20, 250),
    ('MACARONS', 11.88, 72, 300),
    ('MADELEINES', 11.5, 100, 250),
    ('POTATO GRATIN', 12.69, 40, 120)
]


def presentation():
    return(
        print("#################################"),
        print("#                               #"),
        print("#  #######  ## ##     ## ##     #"),
        print("#    ##     ##   ##   ##   ##   #"),
        print("#    ##     ##    #   ## ##     #"),
        print("#    ##     ##   ##   ##        #"),
        print("#    ##     ## ##     ##        #"),
        print("#                       BU ASIA #"),
        print("#################################")
    )


presentation()


def FetchProcess():
    return (
        print("  _    _   __           ___   __ "),
        print(' |_)  |_  (_   | |  |    |   (_  .'),
        print(" | \  |_  __)  |_|  |_   |   __) ."),
        print('')
    )


def FetchHeaderSrp():
    return (
        print("  __   _    _  "),
        print(" (_   |_)  |_) ."),
        print(" __)  | \  |   ."),
        print('')
    )


def FetchMenuHeader():
    return (
        print("        _             "),
        print(" |\/|  |_  |\ |  | | ."),
        print(" |  |  |_  | \|  |_| ."),
        print('')
    )


def FetchMenu():
    return (
        FetchMenuHeader(),
        print("'0' : Exit the program"),
        print("'1' : Keep same data but choose another product"),
        print("'2' : Make a new request"),
        print('')
    )


def NewRequestTitle():
    return (
        print('        _             _        ___   _        '),
        print(' |\ |  |_  \    /    |_  |\ |   |   |_)  \_/ .'),
        print(' | \|  |_   \/\/     |_  | \|   |   | \   |  .')
    )


def display_product(produit):
    count = 0
    print('>>>>>>> Item List')
    while count < len(produit):
        print(str(count) + ' - ' + produit[count][0])
        count += 1
    print('')


def fetch_name(produit):
    icode = int(input("Please enter code product : "))
    count = 0
    name = ""
    for count in range(len(produit)):
        # print(count)
        if count == icode:
            name = produit[count][0]
            return name
        count += 1


def display_country(logcost):
    count = 0
    print('>>>>>>> Shipping Country')
    while count < len(logcost):
        print(str(count) + ' - ' + logcost[count][0])
        count += 1
    print('')


def fetch_name_country(logcost):
    ctr = int(input("Please enter country code : "))
    count = 0
    while count < len(logcost):
        if count == ctr:
            ctr = logcost[count][0]
            return ctr
        count += 1


def calculation(icode, ctr, margin, margin_distrib, margin_retailer):
    i = 0
    # print(len(produit))
    # print(len(produit[1]))
    for i in range(len(produit)):
        for j in range(len(produit[i])):
            # print(produit[i][j])
            if icode == produit[i][j]:
                product_name = produit[i][0]
                pc_res = produit[i][1]
                pcctn_res = produit[i][2]
                ctnpal_res = produit[i][3]
                i = 0
                for i in range(len(logcost)):
                    for j in range(len(logcost[i])):
                        if ctr == logcost[i][j]:
                            country_name = logcost[i][0]
                            fobcost = logcost[i][1]
                            cifcost = logcost[i][2]
                            custom_tax = logcost[i][3]
                            vat = logcost[i][4]
                            currency = logcost[i][5]
                            currency_symbol = logcost[i][6]
                            cost_pallet = logcost[i][7]
                pv = round(pc_res * (1 + (int(margin)/100)), 3)
                pvp = round(pv/pcctn_res, 2)
                total = container * ctnpal_res * pcctn_res
                total_amount = round(container * ctnpal_res * pv, 2)
                fob_p_ctn = round(pv+(fobcost/(container*ctnpal_res)), 3)
                fob_p_pc = round(fob_p_ctn/pcctn_res, 3)
                insurance_cost = round(total_amount * insurance, 2)
                cif_p_ctn = round(
                    pv+(((cifcost+fobcost)+insurance_cost)/(container*ctnpal_res)), 3)
                log_cost_perc = round(((cif_p_ctn-pv)/cif_p_ctn)*100, 2)
                finalprice_pc = round(cif_p_ctn/pcctn_res, 3)
                price_after_ct = round(cif_p_ctn+(cif_p_ctn*custom_tax), 2)
                price_after_vat = round(
                    price_after_ct+(price_after_ct*vat), 2)
                pv_distrib = round(
                    (price_after_vat*currency)/pcctn_res, 3)
                log_cost_percentage = round(
                    cost_pallet/(ctnpal_res*pcctn_res*pv_distrib), 2)
                log_cost_value_retailer = round(
                    (1-(1*(margin_retailer/100))), 2)
                log_cost_value_distrib = round((
                    log_cost_value_retailer-(log_cost_value_retailer*(margin_distrib/100))), 2)
                log_cost_value_transport = (
                    log_cost_value_distrib-(log_cost_value_distrib*(log_cost_percentage)))
                log_value_ratio = round(1/log_cost_value_transport, 2)
                srp = round(pv_distrib*log_value_ratio, 2)
                return (
                    print(x.strftime("%x %X")),
                    print(str(product_name) + " imported in " +
                          str(country_name) + " at " + str(margin) + " % margin : "),
                    print("Total for " + str(container) + " pallets : " + str(total) +
                          " pieces and " + str(total/pcctn_res) + " cases."),
                    print("(EXW) Total amount (" + str(container) + " pallets) : " +
                          str(total_amount) + " euro."),
                    print("(EXW) Price per ctn : " + str(pv)),
                    print("(EXW) Price per pc : " + str(pvp)),
                    print("(FOB) Price per ctn : " +
                          str(fob_p_ctn) + " euro."),
                    print("(FOB) Price per pc : " + str(fob_p_pc) + " euro."),
                    print("(CIF) Price per ctn : " +
                          str(cif_p_ctn) + " euro."),
                    print("(CIF) Final price per pc : " +
                          str(finalprice_pc) + " euro."),
                    print("(CIF) Logistic cost : " +
                          str(log_cost_perc) + " %."),
                    FetchHeaderSrp(),
                    print('Custom tax : ' + str(custom_tax * 100) +
                          "% + VAT : " + str(vat * 100) + "% --> DD price (ctn): " + str(price_after_vat) + " euro."),
                    print(str(round(log_cost_percentage * 100, 2)) +
                          "%"" (Logistic cost)"' and ' + str(log_value_ratio) + " (Cost ratio) "),
                    print('Recommended SRP (1 pc) : ' +
                          str(srp) + " " + currency_symbol),
                )


def input_user():
    display_product(produit)
    icode = fetch_name(produit)
    while icode == None:
        display_product(produit)
        print("/!\ This product doesn't exist ! ")
        icode = fetch_name(produit)
    print('')
    display_country(logcost)
    ctr = fetch_name_country(logcost)
    while ctr == None:
        display_country(logcost)
        print("/!\ This country doesn't exist ! ")
        ctr = fetch_name_country(logcost)
    print('')
    margin = float(input("Enter your margin (ie : 20, 30, 40)) : "))
    margin_distrib = float(
        input("Enter distributor margin (type 0 if None) : "))
    margin_retailer = float(input("Enter retailer margin (type 0 if None) : "))
    FetchProcess()
    calculation(icode, ctr, margin, margin_distrib, margin_retailer)
    FetchMenu()
    user_input = int(input("Please enter : "))
    while user_input == 1:
        display_product(produit)
        icode = fetch_name(produit)
        while icode == None:
            display_product(produit)
            print("/!\ This product doesn't exist ! ")
            icode = fetch_name(produit)  # ici
        FetchProcess()
        calculation(icode, ctr, margin, margin_distrib, margin_retailer)
        FetchMenu()
        user_input = int(input("Please enter : "))
        print('')
    if user_input == 2:
        NewRequestTitle()
        print('')
        input_user()
    else:
        exit()


input_user()

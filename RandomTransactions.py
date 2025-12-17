import pygame
import TestChartGame as tcg
from random import randint, SystemRandom

consumers = [ 200 ] * 300
govtTreasury = 0
govtExpenses = 0
hasSalesTax = False
salesTax = 0.0
hasVatTax = False  #  ??? how to even calculate this?

def main():
    pygame.init()
    SystemRandom()
    w = 1400
    h = 1000
    gray = (127, 127, 127, 255)
    screen = pygame.display.set_mode((w, h), pygame.RESIZABLE)  # pygame.NOFRAME|
    pygame.display.set_caption('Random Transactions w/some Taxes', 'Transaction Sim')
    done = False

    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_k:
                done = True

        display(screen)

        pygame.time.wait(2300)
        pygame.display.flip()
        clock.tick(60)

def display(screen):
    screen.fill((0, 0, 0))
    tcg.drawAxis(screen)
    RunCommerce(500)
    tcg.DrawColumns(screen,consumers)

def TaxEveryone():
    for ndx, person in enumerate(consumers):
        taxAmt = CalcTax(person)
        consumers[ndx] -= taxAmt
        PayTax(taxAmt)

def CalcTax(person):
    return 0

def FlatTax():
    pass

def SalesTax(transaction):
    # global govtTreasury
    tax = transaction * salesTax
    PayTax(tax)
    return tax

percentTax = 0.0
def PercentIncome(income):
    tax = income * percentTax
    PayTax(tax)
    pass

def ProgressiveTax(income):
    tax = income
    PayTax(tax)

def PayTax(tax):
    global govtTreasury
    govtTreasury += tax

def FlatIncome():
    global consumers
    consumers = [ x+5 for x in consumers ]

def RunCommerce(times=100):
    for i in range(times):
        ATransaction()
    #decide how often to run FlatTax() or PercentTax() as in per "annum"
    consumers.sort()
    # global consumers
    # consumers = sorted(consumers)
    print('min =', min(consumers), '\nmax =', max(consumers))
    print('bot 10 \n\t', consumers[:10])
    print('top 10 \n\t', consumers[-10:])

def ATransaction():
    buyer = randint(0,len(consumers)-1) # randint(n,m)  a no. from n to m inclusive
    if consumers[buyer] <= 0: return

    amt = randint(0,consumers[buyer])
    if hasSalesTax:
        amt += SalesTax(amt)
    seller = randint(0,len(consumers)-1)
    while buyer == seller:
        seller = randint(0, len(consumers) - 1)

    consumers[buyer] -= amt
    consumers[seller] += amt

if __name__ == "__main__":
    main()

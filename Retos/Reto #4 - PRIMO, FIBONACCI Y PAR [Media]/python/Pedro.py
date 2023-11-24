#  * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
#  * Ejemplos:
#  * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
#  * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
#  */

def fib_prim_pa(n):
    if n % 2 == 0:
        par = "es par"
    else:
        par = "es impar"
    lista_fibonacci = [0,1]
    for i in range(n+2):
        lista_fibonacci.append(lista_fibonacci[i-1] + lista_fibonacci[i])
    if n in lista_fibonacci:
        fibonacci = "es fibonacci"
    else:
        fibonacci = "no es fibonacci"
    for i in range(2,n):
        if n/i == 0:
            primo = "no es primo"
        else:
            primo = "es primo"
    print(par + ", " + fibonacci + "; " + primo)

fib_prim_pa(10000)

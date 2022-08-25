given_string = """One morning, when Gregor Samsa woke from troubled dreams, 
he found himself transformed in his bed into a horrible vermin.
He lay on his armour-like back, and if he lifted his head a 
little he could see his brown belly, slightly domed and divided by 
arches into stiff sections. The bedding was hardly able to cover 
it and seemed ready to slide off any moment. His many legs, pitifully 
thin compared with the size of the rest of him, waved about helplessly 
as he looked."""

gregor_index=given_string.index("Gregor")#used to find the index of the first letter of gregor
gregor_indexlength=len("Gregor")#used to find the length of string
gregor_ind=gregor_index+gregor_indexlength#used to find the length for the frst to last letter of 
Gregor=given_string[gregor_index:gregor_ind]#prints gregor
print(Gregor)
H_index=given_string.index("H")
E_index=given_string.index("e")
LL_index=given_string.index("l")
O_index=given_string.index("o")
Hello=given_string[H_index] + given_string[E_index] +given_string[LL_index]+given_string[LL_index] +given_string[O_index]
print(Hello,Gregor)

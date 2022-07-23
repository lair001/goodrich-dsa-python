If the parameter to the make payment method of the CreditCard class
were a negative number, that would have the effect of _raising_ the balance
on the account. Revise the implementation so that it raises a ValueError if
a negative value is sent.
# SBI_IFSC_Code

dependencies = {
request,fuzzywuzzy,bs4
}

This script lets you get IFSC code of SBI branches all over the India. You have to give query in the form STATE+DISTRICT+BRANCHNAME. It matches the branch name using fuzzywuzzy algorithm. So small typos will still give you results.

# Usage

```python
from Ifsc import Ifsc
query = Ifsc("Maharashtra+jalgaon+ereandol")
#the correct name is Erandol, but small typos for branch names can still give you correct results.
print(query.get_code())
```

# Example RUN

```
Original Query:  Maharashtra jalgaon ereandol
Normalized Query:  MAHARASHTRA JALGAON ERANDOL
Full URL:  https://bankifsccode.com/STATE_BANK_OF_INDIA/MAHARASHTRA/JALGAON/ERANDOL/
SBIN0001207
```


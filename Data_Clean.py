def Basics_Search(des):
    find_heads = des.head()
    print(f"\nFind Five Rows:\n{find_heads}")
    informations = des.info()
    print(f"\nDataset Info: \n{informations}")

def describe(des):
    details = des.describe()
    print(f"\nDescibe Dataset: \n{details}")

def Missvalues(des):
    miss1 = des.isnull().sum()
    print(f"\nMissing Values:\n {miss1}")

def DropDuplicates(des):
    drops_values = des.dropna().drop_duplicates().isnull().sum()
    print(f"\nCleaned Data:\n {drops_values}")

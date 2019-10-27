from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

link = 'https://www.emag.ro/label/Top-business?ref=hp_menu_quick-nav_463_17&type=link'    
page = uReq(link)
page_html = page.read()
page.close()
page_soup = soup(page_html, 'html.parser')

#Produs 1
#nume carte 
nume = page_soup.find('a', {'class' :'product-title js-product-url'})
nume_carte = nume['title']
print(nume_carte)

#pret
pret = page_soup.find('p', {'class' :'product-new-price'})
pret2 = pret.text
print(pret2)

# daca e in stoc sau nu
stoc = page_soup.find('p', {'class' :'product-stock-status text-availability-in_stock'})
stoc2 = stoc.text.strip()
print(stoc2)

# procent reducere
reducere = page_soup.find('span', {'class' :'product-this-deal'})
reducere2 = reducere.text.strip()
print(reducere2)


#Produs 2
link = 'https://www.emag.ro/cel-mai-sanatos-om-din-lume-a-j-jacobs-9786068560328/pd/DRDXMMBBM/?X-Search-Id=1cfc38cd1a14bbbd2bb9&X-Product-Id=11094496&X-Search-Page=1&X-Search-Position=1&X-Section=search&X-MB=0&X-Search-Action=view'    
page = uReq(link)
page_html = page.read()
page.close()
page_soup = soup(page_html, 'html.parser')

# Numele cartii si autorul
nume_autor = page_soup.find('h1', {'class' :'page-title'})
nume_autor2 = nume_autor.text
print(nume_autor2)

# Pret
pret_produs = page_soup.find('p', {'class' :'product-new-price'})
pret_produs2 = pret_produs.text
print(pret_produs2)

# Cod produs
cod_produs = page_soup.find('span', {'class' :'product-code-display pull-left'})
cod_produs2 = cod_produs.text
print(cod_produs2)
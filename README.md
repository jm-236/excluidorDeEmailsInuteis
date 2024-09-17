# Excluidor de Emails

Este repositório contém dois scripts Python ([`excluispam.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2FCynthia%2FOneDrive%2FDocumentos%2FGitHub%2FexcluidorDeEmailsInuteis%2Fexcluispam.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22d6501c35-8bfb-4e9b-8faf-1749e707db66%22%5D "c:\Users\Cynthia\OneDrive\Documentos\GitHub\excluidorDeEmailsInuteis\excluispam.py") e [`script.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2FCynthia%2FOneDrive%2FDocumentos%2FGitHub%2FexcluidorDeEmailsInuteis%2Fscript.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22d6501c35-8bfb-4e9b-8faf-1749e707db66%22%5D "c:\Users\Cynthia\OneDrive\Documentos\GitHub\excluidorDeEmailsInuteis\script.py")) que utilizam a biblioteca [`pyautogui`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2FCynthia%2FOneDrive%2FDocumentos%2FGitHub%2FexcluidorDeEmailsInuteis%2Fscript.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A7%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2FCynthia%2FOneDrive%2FDocumentos%2FGitHub%2FexcluidorDeEmailsInuteis%2Fexcluispam.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A7%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2FCynthia%2FOneDrive%2FDocumentos%2FGitHub%2FexcluidorDeEmailsInuteis%2Fscript.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A7%7D%7D%5D%2C%22d6501c35-8bfb-4e9b-8faf-1749e707db66%22%5D "Go to definition") para automatizar a exclusão de e-mails no Gmail. Ambos os scripts abrem o navegador Google Chrome, navegam até a caixa de entrada do Gmail e realizam uma série de ações para selecionar e excluir e-mails de diferentes abas (Promoções e Social).

## Pré-requisitos

- Python 3.x
- Biblioteca [`pyautogui`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2FCynthia%2FOneDrive%2FDocumentos%2FGitHub%2FexcluidorDeEmailsInuteis%2Fscript.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A7%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2FCynthia%2FOneDrive%2FDocumentos%2FGitHub%2FexcluidorDeEmailsInuteis%2Fexcluispam.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A7%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2FCynthia%2FOneDrive%2FDocumentos%2FGitHub%2FexcluidorDeEmailsInuteis%2Fscript.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A7%7D%7D%5D%2C%22d6501c35-8bfb-4e9b-8faf-1749e707db66%22%5D "Go to definition")
- Navegador Google Chrome

Para instalar a biblioteca [`pyautogui`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2FCynthia%2FOneDrive%2FDocumentos%2FGitHub%2FexcluidorDeEmailsInuteis%2Fscript.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A7%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2FCynthia%2FOneDrive%2FDocumentos%2FGitHub%2FexcluidorDeEmailsInuteis%2Fexcluispam.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A7%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2FCynthia%2FOneDrive%2FDocumentos%2FGitHub%2FexcluidorDeEmailsInuteis%2Fscript.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A0%2C%22character%22%3A7%7D%7D%5D%2C%22d6501c35-8bfb-4e9b-8faf-1749e707db66%22%5D "Go to definition"), execute:
```bash
pip install pyautogui
```

## excluispam.py

Este script automatiza a exclusão de e-mails na aba "Spam" do Gmail.

### Passos realizados pelo script:

1. Abre o menu Iniciar do Windows.
2. Digita "chrome" e pressiona Enter para abrir o Google Chrome.
3. Aguarda 2 segundos para o navegador abrir.
4. Navega até a URL do Gmail.
5. Aguarda 5 segundos para a página carregar.
6. Navega até a aba "Mais" no Gmail.
7. Seleciona a aba "Spam".
8. Seleciona todos os e-mails na aba "Spam".
9. Exclui os e-mails selecionados.

## script.py

Este script automatiza a exclusão de e-mails nas abas "Promoções" e "Social" do Gmail.

### Passos realizados pelo script:

1. Abre o menu Iniciar do Windows.
2. Digita "chrome" e pressiona Enter para abrir o Google Chrome.
3. Aguarda 2 segundos para o navegador abrir.
4. Navega até a URL do Gmail.
5. Aguarda 5 segundos para a página carregar.
6. Navega até a aba "Promoções".
7. Seleciona todos os e-mails na aba "Promoções".
8. Exclui os e-mails selecionados.
9. Navega até a aba "Social".
10. Seleciona todos os e-mails na aba "Social".
11. Exclui os e-mails selecionados.

## Como usar

1. Certifique-se de que o Google Chrome está instalado e configurado como navegador padrão.
2. Execute o script desejado ([`excluispam.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2FCynthia%2FOneDrive%2FDocumentos%2FGitHub%2FexcluidorDeEmailsInuteis%2Fexcluispam.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22d6501c35-8bfb-4e9b-8faf-1749e707db66%22%5D "c:\Users\Cynthia\OneDrive\Documentos\GitHub\excluidorDeEmailsInuteis\excluispam.py") ou [`script.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fc%3A%2FUsers%2FCynthia%2FOneDrive%2FDocumentos%2FGitHub%2FexcluidorDeEmailsInuteis%2Fscript.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22d6501c35-8bfb-4e9b-8faf-1749e707db66%22%5D "c:\Users\Cynthia\OneDrive\Documentos\GitHub\excluidorDeEmailsInuteis\script.py")) usando o Python:
   ```bash
   python excluispam.py
   ```
   ou
   ```bash
   python script.py
   ```

## Aviso

- Esses scripts simulam ações de teclado e mouse, portanto, é importante não usar o computador enquanto os scripts estão em execução para evitar interferências.
- Certifique-se de que a resolução da tela e a interface do Gmail não mudem, pois isso pode afetar a precisão dos scripts.

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou correções. Faça um fork deste repositório, crie uma branch para suas alterações e envie um pull request.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.

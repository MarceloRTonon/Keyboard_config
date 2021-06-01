# Configuração das teclas do meu teclado

Como o nome já indica: simplesmente a configuração do meu teclado! Estou fazendo para o meu uso pessoal, para que eu possa então manter a salvo se alguma coisa acontecer com o meu pc (e eu simplesmente não conseguir recuperar as configurações). Também para caso alguém queira usar o meu teclado, ter uma colinha fácil. Se vocẽ quiser tentar para o seu próprio uso, ou mesmo para criticar, por favor, sinta-se a vontade. Apenas leia o guia logo após o pequeno aviso em inglẽs. 

As configurações estão todas para Linux (Ubuntu), usando o programa Autokey próprio para Linux. No entanto também precisei usar outros programas como o Gnome Tweak Tool, pois modifiquei o teclado. Não descarto no futuro, colocar mais disponibilidades de teclados ou para outro programas e sistemas operacionais. Vai depender da minha necessidade pessoal, ou mesmo se, dada a sugestão de outra pessoa, é algo simples de se fazer.

Por enquanto, só tenho configurações próprias para o teclado 60% com ABNT (formato brasileiro com ç, ' e \`). Ou seja, se você é como eu, um usuário do **Linux** que comprou o teclado **Husky Blizzard TC-HBL 60% ABNT** (seja o preto, TC-HBL-RA, o branco, TC-HBL-BR, ou o rosa, TC-HBL-RO), e não ficou 100% satisfeito com o gerênciamento de camadas, como na hora de usar as tecladas direcionais e as de navegação (`Delele`, `Home`, `End` e etc), talvez isso daqui te ajude. Ou mesmo se ficou satisfeito, saiba que ele pode ser melhorado. Boa parte do que eu fiz até agora é pensando nesse teclado em específico, até porque ele é o único compacto ABNT que tem por aí, tentando manter uma consistência com o que vem escrito nas suas teclas. Os compromissos feitos são poucos nesse sentido até então. Pode ser que eu mude ao longo do tempo. Vale notar no entanto, que é possível manter tudo que está aí num teclado TKL ou mesmo 100% por exemplo. Outro ponto importante, é que eu o fiz tentando adotar a filosofia das duas mãos trabalharem juntas ao mesmo tempo, e tentando evitar ao máximo uma torção da mão, ou algo assim.

Vou ir escrevendo esse tutorial aos poucos. Adicionando as coisas e os passos necessarios. Depois do Breve comentário em inglês abaixo, resumindo o que quero fazer. O texto está todo na metade, pois estou muito ocupado agora.

# Keyboard Key Configuration

As the name suggests: the configuration of my keyboard. Done for my personal use, so I can keep it safe if anything happen to my pc (and I cannot retrive it). If you want try using it for yourself or even to criticize or make any suggestions, by **ALL MEANS, be my guest!** At first, I plan to write only a extensive portuguese explanation, since I imagine most people who are going to read this are portuguese speakers, specially because now I am dealing with a Keyboard with a Brazilian Layout.

For now it has only the 60% format for ABNT (Brazilian Layout) and in Linux AutoKey. There are a few good codes out there using Linux AutoKey for stuff that I do here.

# Sobre o OS

Se você usa outro que não o Ubuntu pode ser que você precise de seguir outro caminho especialmente se o seu desktop for baseado em Qt e não em gtk, se tiver problemas, veja essa parte na [página]{https://github.com/autokey/autokey#installation} do repositório do Autokey ou na [wiki]{https://github.com/autokey/autokey/wiki/Installing} deles se precisar de algo bem detalhado.

**Além disso** algumas funções tem variantes específicas para `gtk` e para `Qt`! Nada que adicionar uma palavrinha aqui e ali não resolva.
## Preparando o PC

Vamos primeiramente instalar o Autokey. No caso do ubuntu ou de sistema com desktops `gtk-based` você pode fazer pelo package manager ou pelo terminal mesmo:
```console
sudo apt-get update
sudo apt-get install autokey-gtk
```

Se o seu sistema tiver um `Qt-based desktop envinroment` vá na [wiki]{https://github.com/autokey/autokey/wiki/Installing}.



## A tecla Hyper

**ESSA PARTE É OPCIONAL, PORÉM RELEVANTE**

Na minha configuração eu uso a todo momento a tecla `Hyper`, que não é configurada automaticamente no `Ubuntu` e em outras distros do Linux (no Windows é o `Ctrl` da direita), se você tá em dúvida se esse é o seu caso vale você fazer o teste. Aqui eu irei explicar como eu transformei o `CAPS LOCK` na tecla `Hyper` (e como faço então para travar em Caixa Alta). Se vocẽ não quiser usar a tecla `Hyper` no seus atalhos, tudo bem, você só irá precisar **alterar manualmente todos as configurações do meu código em relação à isso (pois uso e abuso da tecla `Hyper`)**. Se você quiser outra tecla como `Hyper` que não o `CAPS LOCK`, também fique a vontade. Se você até agora não faz ideia do que seja uma tecla `Hyper`, veja o parágrafo abaixo, ou [leia aqui]{https://askubuntu.com/questions/19558/what-are-the-meta-super-and-hyper-keys}. Se você sabe, pode até pular.

O seu teclado tem várias teclas especiais, como `Control`, `Alt` e `Alt Gr`. Essas teclas fazem vocẽ acessar "camadas" diferentes do seu teclado. Igual aquela tecla de Função, `Fn`, que muitas vezes vocẽ ignora, mas te faz acessar funções de mídia, ou mesmo as teclas de navegação (`End`, `Home`, `Page Up` e `Page Down`). A chamada tecla "Windows" é no Linux referida como tecla `Super`. O que acontece então é que vamos modificar a tecla `CAPS LOCK` para ela funcionar como uma tecla `Hyper`. 

Para modificar o `CAPS LOCK` eu usei o Gnome Tweak tool, porém existem outras opções como o **Xmodmap** que é mais poderoso e direto pelo terminal (podendo talvez ser melhor para quem use arch?). Eu preferi o Gnome Tweak tool pois achei ele bem seguro e intuitivo e eu tenho medo de fazer muita merda. Pelo terminal você pode instala-lo num sistema Debian/Ubuntu fazendo:

```console
sudo apt-get install gnome-tweak tool
```

Depois é só escrever:

```console
gnome-tweaks
```

Repare que para instalar o `tweak` é sem **s** no final e para rodar é com. Esse comando abrirá uma janela de Ajustes. Nela vá na parte escrita `Teclado & Mouse` e então clique no botão `Opções adicionais de Layout` que abrirá uma nova janela com o mesmo nome do botão. Nela vocẽ quer mudar duas configurações:

 - Em `Comportamento do Caps Lock` você quer mudar para `Fazer do Caps Lock um Hyper`.
 - Em `Opções Variadas de Compatibilidade` assinale a opção `Ambos Shift juntos habilitam o Caps Lock`

Agora para travar o texto em caixa alta vocẽ irá pressionar o Shift direito e esquerdo juntos. A tecla `Caps Lock` que fazia isso será agora a sua tecla `Hyper`.

### Funcionalidades escondidas com Hyper

O interessante quando você configura uma tecla `Hyper` é que você descobre uma série de atalhos já prontos pelo próprio sistema. O que não deixa de ser engraçado se pensarmos que no Ubuntu não há uma tecla `Hyper` previamente configurada. No meu caso eu cansei de descobrir algumas teclas e que às vezes entram em conflito com coisas que eu quero fazer. Algumas funcionalidades que descubro eu inclusive não mexo pois achei interessante. Porém tem várias que eu ainda não consegui alterar pois: não sei mexer.

# Sobre Jogos e o Teclado 60%

A parte de entrar em conflito pode ser real quando você quer fazer coisas especificas. Isso é muito real para mim quando vou jogar algumas, pois algumas alterações do dia a dia não me são desejáveis na hora de jogar e algumas alterações especificas eu só quero para jogar. Inclusive: existe muitas formas de você usar o Autokey para automatizar tarefas em jogos. Eu não faço isso, pois é trapaça e deixa o jogo sem graça, mas existe... Eu apenas realoco teclas que são muito ruins para digitar usando o meu teclado 60%.

Como eu já disse: muitas teclas que eu estou configurando se dão pelo meu teclado em específico.

# Alterações no 60%

**\[ À especificar \]**

# Alterações Acadêmicas

**\[ À especificar \]**

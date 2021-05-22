# Configuração das teclas do meu teclado

Como o nome já indica: simplesmente a configuração do meu teclado! Estou fazendo para o meu uso pessoal, para que eu possa então manter a salvo se alguma coisa acontecer com o meu pc (e eu simplesmente não conseguir recuperar as configurações). Também para caso alguém queira usar o meu teclado, ter uma colinha fácil. Se vocẽ quiser tentar para o seu próprio uso, ou mesmo para criticar, por favor, sinta-se a vontade. Apenas leia o guia logo após o pequeno aviso em inglẽs. 

As configurações estão todas para Linux (Ubuntu), usando o programa Autokey próprio para Linux. No entanto também precisei usar outros programas como o Gnome Tweak Tool, pois modifiquei o teclado. Não descarto no futuro, colocar mais disponibilidades de teclados ou para outro programas e sistemas operacionais. Vai depender da minha necessidade pessoal, ou mesmo se, dada a sugestão de outra pessoa, é algo simples de se fazer.

Por enquanto, só tenho configurações próprias para o teclado 60% com ABNT (formato brasileiro com ç, ' e \`). Ou seja, se você é como eu, um usuário do **Linux** que comprou o teclado **Husky Blizzard TC-HBL 60% ABNT** (seja o preto, TC-HBL-RA, o branco, TC-HBL-BR, ou o rosa, TC-HBL-RO), e não ficou 100% satisfeito com o gerênciamento de camadas, como na hora de usar as tecladas direcionais e as de navegação (`Delele`, `Home`, `End` e etc), talvez isso daqui te ajude. Ou mesmo se ficou satisfeito, saiba que ele pode ser melhorado. Boa parte do que eu fiz até agora é pensando nesse teclado em específico, até porque ele é o único compacto ABNT que tem por aí, tentando manter uma consistência com o que vem escrito nas suas teclas. Os compromissos feitos são poucos nesse sentido até então. Pode ser que eu mude ao longo do tempo. Vale notar no entanto, que é possível manter tudo que está aí num teclado TKL ou mesmo 100% por exemplo. Outro ponto importante, é que eu o fiz tentando adotar a filosofia das duas mãos trabalharem juntas ao mesmo tempo, e tentando evitar ao máximo uma torção da mão, ou algo assim.

Vou ir escrevendo esse tutorial aos poucos. Adicionando as coisas e os passos necessarios. Depois do Breve comentário em inglês abaixo, resumindo o que 

# Keyboard Key Configuration

As the name suggests: the configuration of my keyboard. Done for my personal use, so I can keep it safe if anything happen to my pc (and I cannot retrive it). If you want try using it for yourself or even to criticize or make any suggestions, by **ALL MEANS, be my guest!** At first, I plan to write only a extensive portuguese explanation, since I imagine most people who are going to read this are portuguese speakers, specially because now I am dealing with a Keyboard with a Brazilian Layout.

For now it has only the 60% format for ABNT (Brazilian Layout) and in Linux AutoKey. There are a few good codes out there using Linux AutoKey for stuff that I do here.

# Ubuntu
## Preparando o PC

Vamos primeiramente instalar o Autokey. No caso do ubuntu é:
```console
sudo apt-get update
sudo apt-get install autokey-gtk
```

O primeiro compromisso que iremos fazer é tirar da tecla CAPS LOCK a função de trava de caixa alta. Ela será uma tecla modificadora, a chamada tecla `Hyper`. Agora será apertando os dois shifts ao mesmo tempo que irá travar os carácteres em caixa alta.
O que eu fiz foi usar o Gnome Tweak tool, porém ex. Pelo terminal você pode instalar como:

```console
sudo apt-get install gnome-tweak tool```

Depois é 

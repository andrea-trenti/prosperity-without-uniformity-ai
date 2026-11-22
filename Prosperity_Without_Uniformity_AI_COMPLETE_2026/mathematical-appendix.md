# Appendice matematica — Benessere, diversità, AI, prezzi e ricomposizione del lavoro

**Status delle formule:** modelli **proposti per verificare** le intuizioni dell'autore. Non si tratta di formule enunciate, stimate, dimostrate o approvate dall'autore nei vocali o nel messaggio del 22 novembre 2026. I numeri degli esempi contrassegnati **[ILL]** sono puramente illustrativi e riproducibili. Le osservazioni empiriche sono nel `references.md`.

## A. Funzione obiettivo della teoria generale (vocali del 2 novembre)

Si può iniziare da un vettore di risultati anziché da un unico indice arbitrario:

\[
\mathbf z(p) = \left(W(p),\, D_{+}(p),\, F(p),\, R(p)\right),
\]

dove \(p\) è il vettore di politiche, \(W\) il benessere collettivo, \(D_+\) una misura di diversità valutata positivamente, \(F\) una misura di opportunità e diritti equamente accessibili, \(R\) la capacità delle istituzioni di rispondere e correggersi. **Solo le idee generali di benessere, diversità e correzione adattiva sono pronunciate nei vocali**: la specifica vettoriale è redazionale. Il modo più prudente di procedere è cercare la **frontiera di Pareto** e poi rendere esplicite le preferenze sociali, anziché «dimostrare» che una qualsiasi via di mezzo sia ottimale.

Un'eventuale forma scalare, da stimare o sottoporre a scelta pubblica, potrebbe essere:

\[
\max_{p \in \mathcal P}\quad \lambda_W W(p)+\lambda_D D_+(p)+\lambda_F F(p)-\lambda_C C_\mathrm{trans}(p)
\]

con pesi non negativi dichiarati. **La quota demografica 5–10% citata nei vocali non determina nessuno dei pesi e non è un risultato del modello.**

La diversità ha almeno due dimensioni che possono evolvere in direzioni opposte:

\[
D_{\mathrm{within}}=\text{varietà all'interno di un territorio},\qquad
D_{\mathrm{between}}=\text{differenza fra territori}.
\]

Un mondo con più varietà interna può essere un mondo con comunità più simili fra loro. Il principio di diversità **utile** richiede inoltre distinguere le differenze culturali apprezzate dalle inefficienze chiaramente dannose: non tutte le distanze da un benchmark sono da preservare.

## B. La produttività non coincide con l'occupazione

Definiamo:

\[
A=\frac{Y}{H},
\]

con \(Y\) output corretto e verificato e \(H\) ore di lavoro umano. Se \(Y\) rimane invariato e \(H\) cala, \(A\) cresce; ciò **non implica** che il numero degli occupati nell'intera economia debba aumentare. L'occupazione settoriale approssimativa può essere espressa come:

\[
N = \frac{Qh}{\bar H},
\]

con \(Q\) quantità prodotta, \(h\) ore umane per unità, \(\bar H\) ore per lavoratore. Pertanto:

\[
\frac{N_1}{N_0}=\frac{Q_1}{Q_0}\frac{h_1}{h_0}\frac{\bar H_0}{\bar H_1}.
\]

Se l'AI dimezza le ore per unità e la domanda rimane costante, l'impresa può ridurre il lavoro richiesto anche con produttività raddoppiata.

## C. Dalla quota di compiti automatizzati al costo effettivo

Per evitare l'errore **90% dei task = 90% del prezzo**, separiamo le componenti del costo unitario:

\[
C_0=L_0+M_0+F_0/Q_0,
\]

\[
C_1=L_0(1-sa)+M_0+A_\mathrm{AI}+V_\mathrm{audit}+F_1/Q_1.
\]

* \(s\in[0,1]\): quota di **ore/lavoro umano iniziali** attribuibile ad attività esposte;
* \(a\in[0,1]\): frazione di queste ore realmente risparmiate **al netto delle correzioni**;
* \(L_0\): costo umano unitario iniziale;
* \(M_0\): altri costi variabili non sostituiti;
* \(A_\mathrm{AI}\): costo di modelli, calcolo e infrastrutture per unità;
* \(V_\mathrm{audit}\): costo di validazione, compliance e controllo;
* \(F/Q\): quota di costi fissi.

Se si automatizza il \(90\%\) del tempo di lavoro ma il costo del lavoro iniziale rappresenta solo il \(50\%\) del costo totale e ogni altra cosa rimane costante, **il limite superiore del risparmio è il 45%**, prima dei nuovi costi di AI, non il 90% del prezzo.

### Esempio con una consulenza [ILL]

Prezzo iniziale: \(P_0=€1.000\). Costi variabili iniziali \(L_0=€400\), \(M_0=€200\) e nessun fisso per semplicità: \(C_0=€600\), margine lordo unitario \(€400\). Con \(s=1\), \(a=0{,}9\), \(A_\mathrm{AI}=€40\) e \(V_\mathrm{audit}=€30\):

\[
C_1=400(1-0.9)+200+40+30=€310.
\]

Se il prezzo resta €1.000, il margine unitario passa da **€400 a €690**; se la concorrenza riduce il prezzo a **€500**, il margine lordo unitario diventa **€190**. Vendere a **€100** in questo scenario significherebbe perdere **€210 per unità**. L'esempio dell'autore €1.000 → €100 **può** essere possibile in alcune attività, ma solo con una struttura di costi e una dinamica concorrenziale radicalmente diverse: non discende automaticamente da «90% dei compiti».

## D. Pass-through dal costo al prezzo e dinamica dei margini

Definiamo il rapporto di pass-through di lungo periodo per un prodotto:

\[
\rho = \frac{\Delta P}{\Delta C},\qquad \text{per }\Delta C<0,
\]

con differenze **in euro per unità**, non percentuali. Un valore \(\rho=0\) implica nessun trasferimento del risparmio al cliente; \(\rho=1\) equivale a trasferimento uno-a-uno. Il valore dipende da concorrenza, elasticità della domanda, potere di mercato, capacità produttiva e altre condizioni. Non è una costante universale e può anche trovarsi fuori dall'intervallo [0,1] in contesti specifici.

Per rappresentare il ritardo fra adozione e adeguamento dei prezzi si può utilizzare, come **dinamica didattica**:

\[
P_{t+1}=P_t+\kappa(P_t^*-P_t),\qquad 0<\kappa\leq 1,
\]

in cui \(P_t^*\) è il prezzo concorrenziale di riferimento e \(\kappa\) la rapidità di aggiustamento. Il ritardo crea la **finestra di margine iniziale** che l'autore descrive. Il modello è illustrativo; per identificare \(\kappa\) servono dati reali.

Il prezzo reale settoriale è \(P_t/P_t^{CPI}\), mentre **accessibilità rispetto al salario** è \(P_t/w_t\). I due concetti differiscono. La riduzione del prezzo di un singolo servizio non è una deflazione generale.

## E. Prezzi, volumi e fatturato

Assumiamo, solo per lo scenario locale, una domanda a elasticità costante:

\[
Q(P)=Q_0\left(\frac{P}{P_0}\right)^{-\varepsilon},\quad \varepsilon\geq0.
\]

Il ricavo \(R=PQ\) varia secondo:

\[
\frac{R_1}{R_0}=\left(\frac{P_1}{P_0}\right)^{1-\varepsilon}.
\]

**Proposizione condizionata:** se \(P_1<P_0\), il fatturato aumenta **solo quando \(\varepsilon>1\)**; rimane invariato con \(\varepsilon=1\); diminuisce quando \(0\le\varepsilon<1\). Ciò formalizza la previsione dell'autore secondo cui prezzi più bassi *possono* produrre più clienti e anche più fatturato, ma non necessariamente.

### Esempio €1.000 → €100 [ILL]

\(r_P=0{,}1\). Allora:

| Elasticità | Moltiplicatore quantità \(Q_1/Q_0\) | Moltiplicatore ricavi \(R_1/R_0\) | Interpretazione |
|---:|---:|---:|---|
| 0,5 | 3,162× | 0,316× | Più clienti, ricavi molto più bassi |
| 1,0 | 10× | 1,000× | Ricavi invariati |
| 1,2 | 15,849× | 1,585× | Ricavi maggiori malgrado il prezzo ridotto |
| 1,5 | 31,623× | 3,162× | Forte espansione del mercato, con possibile vincolo di capacità |

Questi numeri non stimano l'elasticità della consulenza o del software: mostrano **quali ipotesi la tesi richiede**.

## F. Condizione per recuperare l'occupazione settoriale

Con \(h_1/h_0=r_h\) e ore medie per addetto costanti:

\[
\frac{N_1}{N_0}=\left(\frac{P_1}{P_0}\right)^{-\varepsilon}r_h.
\]

La condizione per avere almeno tanti occupati quante prima nel **medesimo settore** è:

\[
\varepsilon\geq\frac{\ln(1/r_h)}{\ln(P_0/P_1)}
\]

per \(0<r_h<1\) e \(P_1<P_0\). Se prezzo e ore per unità si riducono entrambi del **90%** (entrambi diventano il 10% del valore iniziale), occorre **elasticità almeno pari a 1** affinché la crescita della quantità compensi l'automazione nel solo settore considerato. Con \(\varepsilon=0{,}5\), l'occupazione settoriale passa a circa **31,6%** del livello iniziale; con \(\varepsilon=1{,}2\), salirebbe a circa **158,5%**, sotto ipotesi estremamente forti. Non include nuove professioni esterne, effetti sul reddito né investimenti.

## G. Compiti nuovi e qualità come domanda addizionale

Per non assumere che l'intero lavoro derivi dal vecchio prodotto, introduciamo:

\[
N_{tot,1}=N_{base,1}+N_{new,1}-N_{obsolete,1},
\]

in cui \(N_{new,1}\) rappresenta occupazione nuova per qualità, differenziazione, manutenzione, integrazione, sicurezza, nuovi mercati e prodotti; \(N_{obsolete,1}\) eventuali altri posti eliminati fuori dal settore base. L'equazione è un'**identità contabile**, non una previsione sulla positività del saldo.

Una possibile scomposizione delle decisioni aziendali è:

\[
\max_{q,z,k} \quad \pi = P(q,z,k)\,q-C(q,z,k; AI),
\]

in cui \(z\) indica un vettore di attributi qualitativi, \(k\) il numero di varianti/prodotti (espansione «orizzontale») e la complessità o profondità di \(z\) l'espansione «verticale». La scelta effettiva dipende dalla disponibilità a pagare e dai costi marginali di ciascuna dimensione.

## H. Stipendi nominali, prezzi reali e bisogno di sostegno

Il potere d'acquisto familiare va valutato usando il **reddito disponibile reale**:

\[
y^{real}_{i,t}=\frac{w_{i,t}h_{i,t}+b_{i,t}+r_{i,t}-T_{i,t}}{CPI_t},
\]

con reddito da lavoro \(wh\), trasferimenti \(b\), redditi da capitale \(r\) e imposte \(T\). Per una persona che perde il lavoro \(wh=0\): anche con \(CPI\) inferiore potrebbe esserci una grave perdita di benessere se trasferimenti e altri redditi sono insufficienti. Da ciò **non** deriva automaticamente l'UBI permanente, ma **non** si può negare il bisogno di aiuti transitori usando solo il calo del prezzo dei servizi AI.

Per valutare la tesi UBI occorre specificare: probabilità di ricollocamento, durata della disoccupazione, variazione dei salari reali, quote di rendita del capitale, prezzi del paniere essenziale, costo fiscale di differenti trasferimenti e effetti su partecipazione al lavoro. In questa versione non è stata stimata nessuna di queste grandezze.

## I. Formalizzazione del principio «non andare alla cieca»

Una politica \(p_t\) può essere adattata in funzione di un segnale misurato \(\mathbf s_t\) (occupazione junior, salari, prezzi, qualità, adozione, durata della disoccupazione):

\[
p_{t+1}=\Phi\left(p_t,\mathbf s_t,\widehat{\Delta W}_t\right),
\]

con valutazione documentata degli effetti e controlli istituzionali. Il principio è compatibile con i vocali sulla correzione rapida della pubblica amministrazione e con la richiesta espressa nel discorso AI di non procedere alla cieca. Non è un algoritmo politico già proposto dall'autore.

## J. La relazione AI–diversità come ipotesi da verificare

Introduciamo due effetti contrari:

\[
\Delta D = \underbrace{\Delta D_{\mathrm{new\ varieties}}}_{\text{costo sperimentale inferiore}}
-\underbrace{\Delta D_{\mathrm{standard\ templates}}}_{\text{stesse piattaforme e modelli}}.
\]

Questa formula è una rappresentazione dei meccanismi di **differenziazione tecnica** discussi nell'AI e **convergenza culturale** discussi nei vocali, non la pretesa che la diversità si misuri con una sottrazione empiricamente disponibile. Serve per generare test: numero di prodotti e varianti realmente distinti, concentrazione dei fornitori, differenza fra territori, quota di prodotti creativi uniformi, soddisfazione degli utenti.

## K. Controlli di validità logica e causale

* Una correlazione fra adozione AI e perdita di occupazione junior **non prova causalità**: imprese adottanti possono essere settorialmente diverse o già in ristrutturazione.
* Un RCT che rileva aumento di produttività in un task **non dimostra** che salari e occupazione dell'intera economia aumenteranno.
* Il prezzo \(€1.000\to €100\), il risparmio del 90% e le nuove professioni meglio pagate sono **scenari parlati**; non sono osservazioni empiriche.
* Una riduzione del prezzo di un bene **non implica** deflazione generale dell'indice dei prezzi.
* Una caduta del costo medio unitario **non implica** pass-through ai clienti in mercati non competitivi.
* L'aumento del fatturato non è automatico quando il prezzo scende: dipende dall'elasticità.
* L'occupazione settoriale può diminuire mentre quella aggregata aumenta, e viceversa.
* Nuovi lavori «più complessi» non sono automaticamente accessibili ai lavoratori dislocati.
* Il modello non identifica tassi di automazione, elasticità, probabilità degli scenari o una data di equilibrio.
* La diversità culturale non è equivalente a etnia, apparenza, appartenenza giuridica o diritti individuali.

## Key takeaways

L'elemento quantitativo più importante non è la cifra intuitiva del 90%, ma la **combinazione di quota di costo risparmiabile, grado di pass-through, elasticità della domanda, velocità di adattamento e creazione netta di nuove attività**. È matematicamente possibile che prezzi inferiori e prodotti migliori coesistano con più occupazione; non è dimostrato che debba accadere in ogni settore.

## Analisi future

Stimare \(\rho\) (pass-through) per settori, confrontare elasticità prima/dopo l'adozione, verificare se le aziende che riducono il lavoro base reinvestono in qualità e varietà, misurare percorsi junior→senior, mappare differenziazione locale dei prodotti AI-assisted e condurre una valutazione distributiva dello scenario di lungo periodo.

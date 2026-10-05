# Polityka prywatności: tłumaczenie całego dokumentu (blok) + elementy <head>.
# Gdy zmienisz treść PL, build.py zatrzyma się z nowym hashem: zaktualizuj EN/UK poniżej i wpisz pl_hash.
BOX = 'style="padding: 16px 20px; background: var(--paper-2); border-radius: 8px; border: 1px solid var(--line);"'
LINK = 'style="color: var(--accent-deep);"'

EN = f'''<section class="page-head">
  <div class="wrap">
    <span class="eyebrow">Information document</span>
    <h1>Privacy <em>policy</em></h1>
    <p style="color: var(--ink-2); margin: 0;">Information on the processing of personal data in accordance with Regulation (EU) 2016/679 of the European Parliament and of the Council (GDPR).</p>
    <div class="updated">Last updated: 5 October 2026 · Version 1.2</div>
    <p class="updated">This is a courtesy translation. In case of any discrepancies, the Polish version prevails.</p>
  </div>
</section>

<article>
  <div class="wrap">

    <div class="toc">
      <div class="toc-title">Contents</div>
      <ol>
        <li><a href="#admin">Data controller</a></li>
        <li><a href="#zakres">Scope of data processed</a></li>
        <li><a href="#cele">Purposes and legal bases of processing</a></li>
        <li><a href="#okres">Data retention period</a></li>
        <li><a href="#odbiorcy">Data recipients</a></li>
        <li><a href="#prawa">Rights of the data subject</a></li>
        <li><a href="#cookies">Cookies and tracking technologies</a></li>
        <li><a href="#bezpieczenstwo">Data security</a></li>
        <li><a href="#zmiany">Changes to the Privacy policy</a></li>
        <li><a href="#kontakt">Contact</a></li>
      </ol>
    </div>

    <h2 id="admin">Data controller</h2>
    <p>The controller of your personal data is:</p>
    <p {BOX}>
      <strong>GS Spółka z ograniczoną odpowiedzialnością</strong><br/>
      ul. Płaszowska 25 lok. 1, 30-713 Kraków, Poland<br/>
      Tax ID (NIP): <strong>6793317716</strong> &nbsp;·&nbsp; KRS: <strong>0001144358</strong> &nbsp;·&nbsp; REGON: <strong>540426181</strong><br/>
      Trade name: <strong>Centrum Terapeutyczne Płaszowska 25</strong>
    </p>
    <p>You can contact the Controller about any matter relating to the processing of personal data at <strong>gabinety@plaszowska25.pl</strong> or by phone at <strong>+48 663 433 444</strong>.</p>

    <h2 id="zakres">Scope of data processed</h2>
    <p>Depending on your relationship with the Controller, we may process the following categories of personal data:</p>
    <h3>Room tenants (therapists, specialists)</h3>
    <ul>
      <li>first and last name, business name,</li>
      <li>tax ID (NIP), REGON, business address,</li>
      <li>contact details: email address, phone number,</li>
      <li>billing data (bank account number, invoicing details),</li>
      <li>data on the services provided (professional qualifications, only to the extent necessary).</li>
    </ul>
    <h3>People contacting us via a form or email</h3>
    <ul>
      <li>first and last name,</li>
      <li>email address and/or phone number,</li>
      <li>content of the correspondence.</li>
    </ul>
    <h3>Website users</h3>
    <ul>
      <li>IP address, technical data about the device and browser,</li>
      <li>statistical data on the use of the website (to the extent resulting from cookies).</li>
    </ul>
    <p><strong>The Centre does not process the data of patients</strong> who use the therapy services provided by room tenants. The controller of a patient’s data is the therapist running their practice in the rented room.</p>

    <h2 id="cele">Purposes and legal bases of processing</h2>
    <p>Personal data is processed for the following purposes:</p>
    <ol>
      <li><strong>Concluding and performing the room rental agreement</strong>: legal basis Art. 6(1)(b) GDPR (necessity for the performance of a contract).</li>
      <li><strong>Issuing invoices and settling accounts</strong>: Art. 6(1)(c) GDPR (legal obligation under tax and accounting regulations).</li>
      <li><strong>Responding to enquiries sent via the contact form, the booking enquiry form, the room viewing form or email</strong>: Art. 6(1)(f) GDPR (the Controller’s legitimate interest in handling correspondence). Messages sent through the forms on the website are delivered using the Web3Forms service (see the “Data recipients” section).</li>
      <li><strong>Marketing of our own services: newsletter and email communication</strong>: Art. 6(1)(a) GDPR (consent) in conjunction with Art. 10 of the Polish Act on the Provision of Electronic Services and Art. 172 of the Polish Telecommunications Law. The newsletter is sent via Mailchimp only to people who have given their explicit and voluntary consent (sign-up form or statement). Consent can be withdrawn at any time by clicking the “Unsubscribe” link in the footer of every message or by writing to <strong>gabinety@plaszowska25.pl</strong>.</li>
      <li><strong>Other marketing</strong>: Art. 6(1)(f) GDPR (the Controller’s legitimate interest), only towards people who have expressed interest in the offer.</li>
      <li><strong>Establishing, pursuing or defending claims</strong>: Art. 6(1)(f) GDPR.</li>
      <li><strong>Keeping statistics and improving the website</strong>: Art. 6(1)(f) GDPR and, for analytics cookies, Art. 6(1)(a) GDPR (consent).</li>
    </ol>

    <h2 id="okres">Data retention period</h2>
    <p>Personal data is stored for the following periods:</p>
    <ul>
      <li><strong>Tenant data</strong>: for the duration of the agreement and for the period required by law (including 5 years for accounting records under the Polish Tax Ordinance).</li>
      <li><strong>Correspondence data</strong>: for as long as needed to respond, no longer than 24 months, unless further cooperation is established.</li>
      <li><strong>Marketing data</strong>: until consent is withdrawn or an objection to processing is raised.</li>
      <li><strong>Technical data (cookies)</strong>: for the period specified in the cookie policy of the given tool, up to a maximum of 24 months.</li>
    </ul>

    <h2 id="odbiorcy">Data recipients</h2>
    <p>Your personal data may be shared with the following categories of recipients:</p>
    <ul>
      <li>entities providing accounting, legal and advisory services to the Controller,</li>
      <li>providers of IT, hosting, email, booking and calendar management tools, in particular:
        <ul>
          <li><strong>Google Ireland Limited</strong> (Gordon House, Barrow Street, Dublin 4, Ireland): <strong>Firebase</strong> services (Firestore, Authentication, Cloud Functions, Hosting) used by the Centre’s internal booking management system (CRM), and <strong>Google Analytics 4</strong> used to collect anonymous statistics on the use of the website (only after the User gives consent via the cookie banner). Data may be processed in Google data centres in the European Economic Area and, where necessary, in the United States of America on the basis of standard contractual clauses approved by the European Commission (Commission Implementing Decision 2021/914) and the Data Privacy Framework.</li>
          <li><strong>Intuit Inc. / The Rocket Science Group LLC d/b/a Mailchimp</strong> (675 Ponce de Leon Ave NE, Suite 5000, Atlanta, GA 30308, USA): the <strong>Mailchimp</strong> service used to send marketing correspondence and newsletters to people who have consented to it. Data is transferred on the basis of standard contractual clauses approved by the European Commission and the Data Privacy Framework, under which Mailchimp is registered.</li>
          <li><strong>Meta Platforms Ireland Limited</strong> (4 Grand Canal Square, Grand Canal Harbour, Dublin 2, Ireland): the <strong>Meta Pixel</strong> tool used to measure the effectiveness of ads on Facebook and Instagram and for remarketing, activated only after the User gives consent via the cookie banner. Data (including the IP address and information about activity on the website) may be transferred to Meta Platforms, Inc. in the United States of America on the basis of standard contractual clauses approved by the European Commission and the Data Privacy Framework, under which Meta is registered.</li>
          <li><strong>Web3Creative</strong> (an entity registered in India, Kerala; Udyam registration no. UDYAM-KL-10-0039115): the <strong>Web3Forms</strong> service (<a href="https://web3forms.com" target="_blank" rel="noopener" {LINK}>web3forms.com</a>) used to handle and deliver messages sent through the forms on the website (the contact form, the booking enquiry form and the room viewing form). Web3Forms <strong>does not permanently store the content of submitted forms</strong>: it processes them and forwards them to the Controller’s email address, and server logs containing data are deleted periodically (approximately every 2 months). Data is processed on servers located in the United States of America. Web3Forms acts solely as an intermediary forwarding the form content to the Controller’s email address. The transfer of data to a third country (USA) is necessary to handle the enquiry you submitted, and therefore takes place on the basis of Art. 49(1)(b) GDPR (transfer necessary for the implementation of pre-contractual measures taken at the data subject’s request), as an occasional transfer limited to data you voluntarily provided in the form and not permanently stored by the service provider.</li>
        </ul>
      </li>
      <li>payment operators (for online payments),</li>
      <li>public authorities entitled to request access to data under the law.</li>
    </ul>
    <p>Transfers of data to third countries outside the European Economic Area as part of the <strong>Firebase</strong>, <strong>Mailchimp</strong> and <strong>Meta Pixel</strong> (USA) services take place with the safeguards required by the GDPR, on the basis of standard contractual clauses and the Data Privacy Framework. For the <strong>Web3Forms</strong> service (servers in the USA), used to deliver messages from forms, the transfer is based on the derogation in Art. 49(1)(b) GDPR, as an occasional transfer necessary to handle the enquiry submitted at your request, limited to the data provided in the form and not permanently stored by the service provider.</p>

    <h2 id="prawa">Rights of the data subject</h2>
    <p>You have the following rights under the GDPR:</p>
    <ul>
      <li>the right of access to your data and to obtain a copy (Art. 15 GDPR),</li>
      <li>the right to rectification (Art. 16 GDPR),</li>
      <li>the right to erasure (“the right to be forgotten”, Art. 17 GDPR),</li>
      <li>the right to restriction of processing (Art. 18 GDPR),</li>
      <li>the right to data portability (Art. 20 GDPR),</li>
      <li>the right to object to processing (Art. 21 GDPR),</li>
      <li>the right to withdraw consent at any time, without affecting the lawfulness of processing carried out before its withdrawal,</li>
      <li>the right to lodge a complaint with the President of the Personal Data Protection Office (Prezes UODO, ul. Stawki 2, 00-193 Warsaw, Poland).</li>
    </ul>
    <p>To exercise these rights, please contact us at <strong>gabinety@plaszowska25.pl</strong>.</p>

    <h2 id="cookies">Cookies and tracking technologies</h2>
    <p>The <strong>plaszowska25.pl</strong> website uses cookies, i.e. small text files stored on the user’s device.</p>
    <h3>Types of cookies used</h3>
    <ul>
      <li><strong>Necessary cookies</strong>: required for the website to work properly (including remembering your cookie consent); they do not require consent.</li>
      <li><strong>Analytics cookies (Google Analytics 4)</strong>: used to collect anonymous statistics on the use of the website (number of users, visit duration, popular pages). They require the user’s consent given via the cookie banner. Data collected by GA4 is pseudonymised (with IP anonymisation) and processed by Google Ireland Limited.</li>
      <li><strong>Marketing cookies (Meta Pixel / Facebook)</strong>: the <strong>Meta Pixel</strong> tool provided by Meta Platforms Ireland Limited is used to measure the effectiveness of advertising campaigns on Facebook and Instagram and to show ads to people who have visited the website (remarketing). They require the user’s explicit consent given via the cookie banner and <strong>are not activated without it</strong> or when “Necessary only” is selected. Meta Pixel may set cookies (including <em>_fbp</em>) and transfer data (including the IP address and information about activity on the website) to Meta Platforms, Inc. in the United States.</li>
      <li><strong>Functional cookies</strong>: remember the user’s preferences.</li>
    </ul>
    <p>You can withdraw your consent to cookies at any time by:</p>
    <ul>
      <li>clicking the “Cookie settings” link in the footer of every page of the website, which opens a panel where individual cookie categories can be switched on or off at any time (after consent is withdrawn, we delete the stored analytics and marketing cookies),</li>
      <li>changing the settings of your web browser (including blocking cookies completely).</li>
    </ul>
    <p>Withdrawing consent does not affect the lawfulness of processing carried out before its withdrawal.</p>

    <h2 id="bezpieczenstwo">Data security</h2>
    <p>The Controller applies appropriate technical and organisational measures to ensure the security of the personal data processed, in particular to protect it against disclosure to unauthorised persons, loss, destruction or damage.</p>
    <p>In particular, we use:</p>
    <ul>
      <li>encryption of the connection to the server (SSL/TLS),</li>
      <li>encryption of data at rest in the <strong>Firebase Firestore</strong> database (AES-256),</li>
      <li>multi-factor authentication for people with access to the CRM system,</li>
      <li>regular backups of operational data,</li>
      <li>access control based on the principle of least privilege.</li>
    </ul>

    <h2 id="zmiany">Changes to the Privacy policy</h2>
    <p>The Controller reserves the right to amend this Privacy policy in the event of changes in the law, technology or the scope of its business. The current version of the document is always available at <strong>plaszowska25.pl/polityka-prywatnosci</strong>.</p>

    <h2 id="kontakt">Contact</h2>
    <p>For any matters relating to the processing of personal data, please contact us:</p>
    <ul>
      <li>email: <strong>gabinety@plaszowska25.pl</strong></li>
      <li>phone: <strong>+48 663 433 444</strong></li>
      <li>address: <strong>GS Spółka z ograniczoną odpowiedzialnością, ul. Płaszowska 25 lok. 1, 30-713 Kraków, Poland</strong></li>
    </ul>

  </div>
</article>'''

UK = f'''<section class="page-head">
  <div class="wrap">
    <span class="eyebrow">Інформаційний документ</span>
    <h1>Політика <em>конфіденційності</em></h1>
    <p style="color: var(--ink-2); margin: 0;">Інформація щодо обробки персональних даних відповідно до Регламенту (ЄС) 2016/679 Європейського Парламенту та Ради (GDPR).</p>
    <div class="updated">Дата оновлення: 5 жовтня 2026 р. · Версія 1.2</div>
    <p class="updated">Це переклад для зручності. У разі розбіжностей переважну силу має польська версія.</p>
  </div>
</section>

<article>
  <div class="wrap">

    <div class="toc">
      <div class="toc-title">Зміст</div>
      <ol>
        <li><a href="#admin">Контролер персональних даних</a></li>
        <li><a href="#zakres">Обсяг оброблюваних даних</a></li>
        <li><a href="#cele">Цілі та правові підстави обробки</a></li>
        <li><a href="#okres">Строк зберігання даних</a></li>
        <li><a href="#odbiorcy">Одержувачі даних</a></li>
        <li><a href="#prawa">Права субʼєкта даних</a></li>
        <li><a href="#cookies">Файли cookies і технології відстеження</a></li>
        <li><a href="#bezpieczenstwo">Безпека даних</a></li>
        <li><a href="#zmiany">Зміни до Політики конфіденційності</a></li>
        <li><a href="#kontakt">Контакти</a></li>
      </ol>
    </div>

    <h2 id="admin">Контролер персональних даних</h2>
    <p>Контролером Ваших персональних даних є:</p>
    <p {BOX}>
      <strong>GS Spółka z ograniczoną odpowiedzialnością</strong><br/>
      ul. Płaszowska 25 lok. 1, 30-713 Kraków, Польща<br/>
      Податковий номер (NIP): <strong>6793317716</strong> &nbsp;·&nbsp; KRS: <strong>0001144358</strong> &nbsp;·&nbsp; REGON: <strong>540426181</strong><br/>
      Торгова марка: <strong>Centrum Terapeutyczne Płaszowska 25</strong>
    </p>
    <p>Звʼязатися з Контролером з усіх питань, що стосуються обробки персональних даних, можна за адресою <strong>gabinety@plaszowska25.pl</strong> або за телефоном <strong>+48 663 433 444</strong>.</p>

    <h2 id="zakres">Обсяг оброблюваних даних</h2>
    <p>Залежно від характеру Ваших відносин із Контролером ми можемо обробляти такі категорії персональних даних:</p>
    <h3>Орендарі кабінетів (терапевти, фахівці)</h3>
    <ul>
      <li>імʼя та прізвище, назва підприємницької діяльності,</li>
      <li>NIP, REGON, адреса ведення діяльності,</li>
      <li>контактні дані: адреса електронної пошти, номер телефону,</li>
      <li>дані для розрахунків (номер банківського рахунку, дані для рахунку-фактури),</li>
      <li>дані щодо наданих послуг (професійна кваліфікація, лише в необхідному обсязі).</li>
    </ul>
    <h3>Особи, які звертаються через форму або електронну пошту</h3>
    <ul>
      <li>імʼя та прізвище,</li>
      <li>адреса електронної пошти та/або номер телефону,</li>
      <li>зміст листування.</li>
    </ul>
    <h3>Користувачі вебсайту</h3>
    <ul>
      <li>IP-адреса, технічні дані пристрою та браузера,</li>
      <li>статистичні дані про користування сайтом (в обсязі, що випливає з файлів cookies).</li>
    </ul>
    <p><strong>Центр не обробляє дані пацієнтів</strong>, які користуються терапевтичними послугами орендарів кабінетів. Контролером даних пацієнта є відповідний терапевт, який веде практику в орендованому кабінеті.</p>

    <h2 id="cele">Цілі та правові підстави обробки</h2>
    <p>Персональні дані обробляються з такими цілями:</p>
    <ol>
      <li><strong>Укладення та виконання договору оренди кабінету</strong>: правова підстава ст. 6(1)(b) GDPR (необхідність для виконання договору).</li>
      <li><strong>Виставлення рахунків-фактур і ведення розрахунків</strong>: ст. 6(1)(c) GDPR (юридичний обовʼязок згідно з податковим і бухгалтерським законодавством).</li>
      <li><strong>Відповіді на запити, надіслані через контактну форму, форму запиту на бронювання, форму запису на огляд кабінету або електронною поштою</strong>: ст. 6(1)(f) GDPR (законний інтерес Контролера, що полягає в обробці кореспонденції). Повідомлення, надіслані через форми на сайті, доставляються за допомогою сервісу Web3Forms (див. розділ «Одержувачі даних»).</li>
      <li><strong>Маркетинг власних послуг: розсилка та email-комунікація</strong>: ст. 6(1)(a) GDPR (згода) у поєднанні зі ст. 10 польського Закону про надання послуг електронними засобами та ст. 172 польського Закону про телекомунікації. Розсилка надсилається через сервіс Mailchimp лише особам, які надали на це явну й добровільну згоду (підписка через форму або заява). Згоду можна будь-коли відкликати, натиснувши посилання «Скасувати підписку» у футері кожного листа або написавши на адресу <strong>gabinety@plaszowska25.pl</strong>.</li>
      <li><strong>Інший маркетинг</strong>: ст. 6(1)(f) GDPR (законний інтерес Контролера), лише щодо осіб, які виявили зацікавленість пропозицією.</li>
      <li><strong>Встановлення, пред’явлення або захист від позовів</strong>: ст. 6(1)(f) GDPR.</li>
      <li><strong>Ведення статистики та покращення роботи сайту</strong>: ст. 6(1)(f) GDPR, а в частині аналітичних cookies ст. 6(1)(a) GDPR (згода).</li>
    </ol>

    <h2 id="okres">Строк зберігання даних</h2>
    <p>Персональні дані зберігаються протягом такого строку:</p>
    <ul>
      <li><strong>Дані орендарів</strong>: протягом дії договору та протягом строку, визначеного законодавством (зокрема 5 років для бухгалтерської документації відповідно до польського Податкового кодексу).</li>
      <li><strong>Дані з листування</strong>: протягом часу, необхідного для надання відповіді, але не довше 24 місяців, якщо не буде встановлено подальшої співпраці.</li>
      <li><strong>Маркетингові дані</strong>: до відкликання згоди або заперечення проти обробки.</li>
      <li><strong>Технічні дані (cookies)</strong>: протягом строку, визначеного політикою cookies відповідного інструменту, максимум до 24 місяців.</li>
    </ul>

    <h2 id="odbiorcy">Одержувачі даних</h2>
    <p>Ваші персональні дані можуть передаватися таким категоріям одержувачів:</p>
    <ul>
      <li>субʼєктам, які надають Контролеру бухгалтерські, юридичні та консультаційні послуги,</li>
      <li>постачальникам ІТ-послуг, хостингу, електронної пошти, інструментів бронювання та керування календарем, зокрема:
        <ul>
          <li><strong>Google Ireland Limited</strong> (Gordon House, Barrow Street, Dublin 4, Ірландія): сервіси <strong>Firebase</strong> (Firestore, Authentication, Cloud Functions, Hosting), якими користується внутрішня система керування бронюваннями (CRM) Центру, а також <strong>Google Analytics 4</strong> для збору анонімної статистики користування сайтом (лише після надання згоди Користувачем через банер cookies). Дані можуть оброблятися в центрах обробки даних Google на території Європейської економічної зони та, в необхідному обсязі, у Сполучених Штатах Америки на підставі стандартних договірних положень, затверджених Європейською Комісією (Виконавче рішення ЄК 2021/914), та механізму Data Privacy Framework.</li>
          <li><strong>Intuit Inc. / The Rocket Science Group LLC d/b/a Mailchimp</strong> (675 Ponce de Leon Ave NE, Suite 5000, Atlanta, GA 30308, США): сервіс <strong>Mailchimp</strong> для надсилання маркетингової кореспонденції та розсилок особам, які на це погодилися. Передача даних здійснюється на підставі стандартних договірних положень, затверджених Європейською Комісією, та механізму Data Privacy Framework, у якому Mailchimp зареєстровано.</li>
          <li><strong>Meta Platforms Ireland Limited</strong> (4 Grand Canal Square, Grand Canal Harbour, Dublin 2, Ірландія): інструмент <strong>Meta Pixel</strong> для оцінки ефективності реклами у Facebook та Instagram і для ремаркетингу, який вмикається лише після надання згоди Користувачем через банер cookies. Дані (зокрема IP-адреса та інформація про активність на сайті) можуть передаватися до Meta Platforms, Inc. у Сполучених Штатах Америки на підставі стандартних договірних положень, затверджених Європейською Комісією, та механізму Data Privacy Framework, у якому Meta зареєстровано.</li>
          <li><strong>Web3Creative</strong> (субʼєкт, зареєстрований в Індії, штат Керала; реєстраційний номер Udyam UDYAM-KL-10-0039115): сервіс <strong>Web3Forms</strong> (<a href="https://web3forms.com" target="_blank" rel="noopener" {LINK}>web3forms.com</a>) для обробки та доставки повідомлень, надісланих через форми на сайті (контактна форма, форма запиту на бронювання та форма запису на огляд кабінету). Web3Forms <strong>не зберігає постійно зміст надісланих форм</strong>: він обробляє їх і пересилає на адресу електронної пошти Контролера, а серверні журнали з даними періодично видаляються (приблизно кожні 2 місяці). Дані обробляються на серверах, розташованих у Сполучених Штатах Америки. Web3Forms виконує роль лише посередника, що пересилає зміст форми на адресу електронної пошти Контролера. Передача даних до третьої країни (США) необхідна для обробки надісланого Вами запиту, тому здійснюється на підставі ст. 49(1)(b) GDPR (передача, необхідна для вжиття заходів на запит субʼєкта даних до укладення договору), як разова передача, обмежена даними, добровільно наданими Вами у формі, і не зберігається постачальником постійно.</li>
        </ul>
      </li>
      <li>платіжним операторам (у разі онлайн-розрахунків),</li>
      <li>державним органам, уповноваженим вимагати доступ до даних відповідно до закону.</li>
    </ul>
    <p>Передача даних до третіх країн за межами Європейської економічної зони в рамках сервісів <strong>Firebase</strong>, <strong>Mailchimp</strong> і <strong>Meta Pixel</strong> (США) здійснюється з дотриманням гарантій, яких вимагає GDPR, на підставі стандартних договірних положень і механізму Data Privacy Framework. У випадку сервісу <strong>Web3Forms</strong> (сервери в США), який використовується для доставки повідомлень із форм, передача здійснюється на підставі винятку зі ст. 49(1)(b) GDPR, як разова передача, необхідна для обробки запиту, надісланого на Ваше прохання, обмежена даними, наданими у формі, і не зберігається постачальником постійно.</p>

    <h2 id="prawa">Права субʼєкта даних</h2>
    <p>Відповідно до GDPR Ви маєте такі права:</p>
    <ul>
      <li>право на доступ до даних та отримання їх копії (ст. 15 GDPR),</li>
      <li>право на виправлення даних (ст. 16 GDPR),</li>
      <li>право на видалення даних («право бути забутим», ст. 17 GDPR),</li>
      <li>право на обмеження обробки (ст. 18 GDPR),</li>
      <li>право на перенесення даних (ст. 20 GDPR),</li>
      <li>право на заперечення проти обробки (ст. 21 GDPR),</li>
      <li>право будь-коли відкликати згоду без впливу на законність обробки, здійсненої до її відкликання,</li>
      <li>право подати скаргу Голові Управління із захисту персональних даних Польщі (Prezes UODO, ul. Stawki 2, 00-193 Варшава).</li>
    </ul>
    <p>Для реалізації цих прав просимо звертатися за адресою <strong>gabinety@plaszowska25.pl</strong>.</p>

    <h2 id="cookies">Файли cookies і технології відстеження</h2>
    <p>Вебсайт <strong>plaszowska25.pl</strong> використовує файли cookies, тобто невеликі текстові файли, що зберігаються на пристрої користувача.</p>
    <h3>Види cookies, які ми використовуємо</h3>
    <ul>
      <li><strong>Необхідні cookies</strong>: потрібні для правильної роботи сайту (зокрема для запамʼятовування згоди на cookies), не потребують згоди.</li>
      <li><strong>Аналітичні cookies (Google Analytics 4)</strong>: використовуються для збору анонімної статистики користування сайтом (кількість користувачів, тривалість візиту, популярні сторінки). Потребують згоди користувача, наданої через банер cookies. Дані, які збирає GA4, псевдонімізуються (з анонімізацією IP) і обробляються Google Ireland Limited.</li>
      <li><strong>Маркетингові cookies (Meta Pixel / Facebook)</strong>: інструмент <strong>Meta Pixel</strong> від Meta Platforms Ireland Limited використовується для вимірювання ефективності рекламних кампаній у Facebook та Instagram і для показу реклами людям, які відвідали сайт (ремаркетинг). Потребують явної згоди користувача через банер cookies і <strong>не вмикаються за її відсутності</strong> або в разі вибору «Лише необхідні». Meta Pixel може зберігати cookies (зокрема <em>_fbp</em>) і передавати дані (зокрема IP-адресу та інформацію про активність на сайті) до Meta Platforms, Inc. у США.</li>
      <li><strong>Функціональні cookies</strong>: запамʼятовують налаштування користувача.</li>
    </ul>
    <p>Ви можете будь-коли відкликати згоду на файли cookies, якщо:</p>
    <ul>
      <li>натиснете посилання «Налаштування cookies» у футері будь-якої сторінки сайту: воно відкриває панель, де в будь-який момент можна ввімкнути або вимкнути окремі категорії cookies (після відкликання згоди ми видаляємо збережені аналітичні та маркетингові cookies),</li>
      <li>зміните налаштування свого браузера (зокрема повністю заблокуєте cookies).</li>
    </ul>
    <p>Відкликання згоди не впливає на законність обробки, здійсненої до її відкликання.</p>

    <h2 id="bezpieczenstwo">Безпека даних</h2>
    <p>Контролер застосовує належні технічні та організаційні заходи для забезпечення безпеки оброблюваних персональних даних, зокрема для їх захисту від доступу неуповноважених осіб, втрати, знищення чи пошкодження.</p>
    <p>Зокрема, ми використовуємо:</p>
    <ul>
      <li>шифрування зʼєднання із сервером (протокол SSL/TLS),</li>
      <li>шифрування даних у стані спокою в базі даних <strong>Firebase Firestore</strong> (AES-256),</li>
      <li>багатофакторну автентифікацію для осіб із доступом до системи CRM,</li>
      <li>регулярне резервне копіювання операційних даних,</li>
      <li>контроль доступу за принципом найменших привілеїв (least privilege).</li>
    </ul>

    <h2 id="zmiany">Зміни до Політики конфіденційності</h2>
    <p>Контролер залишає за собою право вносити зміни до цієї Політики конфіденційності у разі зміни законодавства, технологій або обсягу діяльності. Актуальна версія документа завжди доступна за адресою <strong>plaszowska25.pl/polityka-prywatnosci</strong>.</p>

    <h2 id="kontakt">Контакти</h2>
    <p>З усіх питань, повʼязаних з обробкою персональних даних, просимо звертатися:</p>
    <ul>
      <li>e-mail: <strong>gabinety@plaszowska25.pl</strong></li>
      <li>телефон: <strong>+48 663 433 444</strong></li>
      <li>адреса: <strong>GS Spółka z ograniczoną odpowiedzialnością, ul. Płaszowska 25 lok. 1, 30-713 Kraków, Польща</strong></li>
    </ul>

  </div>
</article>'''

BLOCKS = [dict(start='<section class="page-head">', end='</article>', pl_hash='b2768e7b33a613e5', en=EN, uk=UK)]

PAIRS = [
    ('<title>Polityka prywatności | Centrum Płaszowska 25, Kraków</title>',
     '<title>Privacy policy | Płaszowska 25, Kraków</title>',
     '<title>Політика конфіденційності | Płaszowska 25, Краків</title>'),
    ('content="Polityka prywatności Centrum Terapeutycznego Płaszowska 25 w Krakowie: informacje o przetwarzaniu danych osobowych zgodnie z RODO."',
     'content="Privacy policy of the Płaszowska 25 Therapy Centre in Kraków: information on the processing of personal data under the GDPR."',
     'content="Політика конфіденційності терапевтичного центру Płaszowska 25 у Кракові: інформація про обробку персональних даних відповідно до GDPR."'),
    ('"name": "Polityka prywatności"', '"name": "Privacy policy"', '"name": "Політика конфіденційності"'),
]

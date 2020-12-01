import spacy
import re
from spacy.tokenizer import Tokenizer
from collections import Counter
from spacy import displacy
from spacy.matcher import Matcher
#import textacy

nlp = spacy.load("pl_core_news_sm")

# Czytanie stringa
introduction_text = ('This tutorial is about Natural'
                     ' Language Processing in Spacy.')
introduction_doc = nlp(introduction_text)

print([token.text for token in introduction_doc])

# Czytanie z pliku
file_name = 'introduction.txt'
introduction_file_text = open(file_name).read()
introduction_file_doc = nlp(introduction_file_text)

print([token.text for token in introduction_file_doc])

# Wykrywanie zdania
about_text = ('Z małego miasta wielkie sny'
              ' Atakują Twoje ulice'
              ' Wyśniłem sobie Ciebie, gdy'
              ' Śpiewałem głośno pod prysznicem'
              ' Ten ten mój małomiasteczkowy hit'
              ' I małomiasteczkowe słowa'
              ' Ten małomiasteczkowy rytm'
              ' Melodia małomiasteczkowa'
              ' Z małego miasta piękne sny'
              ' Gromadzą się na Twoich ulicach'
              ' Pamiętam, bardzo chciałem tu być'
              ' Na pewno dużo bardziej niż dzisiaj'
              ' Napisał: Dawid Podsiadło')
about_doc = nlp(about_text)
sentences = list(about_doc.sents)
len(sentences)

for sentence in sentences:
    print(sentence)

# "Tokenyzacja" - pozwala na indentyfikację pojedynczych jednostek w tekście
for token in about_doc:
    print(token, token.idx)

# Własna tokenyzacja poprzez aktualizację właściowości tokenizer
prefix_re = spacy.util.compile_prefix_regex(nlp.Defaults.prefixes)
suffix_re = spacy.util.compile_suffix_regex(nlp.Defaults.suffixes)
infix_re = re.compile(r'''[-~]''')


def customize_tokenizer(nlp):
    # Adds support to use `-` as the delimiter for tokenization
    return Tokenizer(nlp.vocab, prefix_search=prefix_re.search,
                     suffix_search=suffix_re.search,
                     infix_finditer=infix_re.finditer,
                     token_match=None
                     )


nlp.tokenizer = customize_tokenizer(nlp)
custom_tokenizer_about_doc = nlp(about_text)
print([token.text for token in custom_tokenizer_about_doc])

# Stop words
spacy_stopwords = spacy.lang.pl.stop_words.STOP_WORDS
len(spacy_stopwords)

for stop_word in list(spacy_stopwords)[:10]:
    print(stop_word)

for token in about_doc:
    if not token.is_stop:
        print(token)

# Lemmatyzacja - proces grupowania odmienionych form słowa, dzięki czemu można je analizować jako pojedynczy element
conference_help_text = ('Mam trzy latka trzy i pół'
                        ' brodą sięgam ponad stół.'
                        ' Mam fartuszek z muchomorkiem'
                        ' do przedszkola chodzę z workiem.')
conference_help_doc = nlp(conference_help_text)
for token in conference_help_doc:
    print(token, token.lemma_)

# Częstotliwość słów - pozwala na analizę najczęściej używanych słów lub unikalnych słów użytych w tekście
complete_text = ('Ten pierwszy raz, mocny bas'
                 ' Szybki pląs po obiedzie'
                 ' Widziałem błysk w obu ślepiach mojej łani, przecież'
                 ' Trzymała mocno tam, gdzie najbardziej lubię'
                 ' Mama mówiła: takie rzeczy tylko po ślubie'
                 ' Wpadli znajomi i z marszu na marsz wzięli'
                 ' Jeden z niebieskich wtedy prawie mnie postrzelił'
                 ' Dobrze wspominam ten jaskrawy czas'
                 ' Chociaż przyznam, że już wyszedłbym zza metalowych krat')

complete_doc = nlp(complete_text)
# Remove stop words and punctuation symbols
words = [token.text for token in complete_doc
         if not token.is_stop and not token.is_punct]
word_freq = Counter(words)
# 5 commonly occurring words with their frequencies
common_words = word_freq.most_common(5)
print(common_words)

# Unique words
unique_words = [word for (word, freq) in word_freq.items() if freq == 1]
print(unique_words)

# Części mowy - wypisuje część mowy do słowa
for token in about_doc:
    print(token, token.tag_, token.pos_, spacy.explain(token.tag_))

# Wizualizacja
about_interest_text = ('On jest zainteresowany w nauce'
                       ' o przetwarzaniu języka natrualnego.')
about_interest_doc = nlp(about_interest_text)


# displacy.serve(about_interest_doc, style='dep')


# Przetwarzanie danych za pomocą funkcji. Ma to na celu przekształcić tekst do formy, którą można analizować.
def is_token_allowed(token):
    """
        Only allow valid tokens which are not stop words
        and punctuation symbols.
    """
    if (not token or not token.string.strip() or
            token.is_stop or token.is_punct):
        return False
    return True


def preprocess_token(token):
    # Reduce token to its lowercase lemma form
    return token.lemma_.strip().lower()


complete_filtered_tokens = [preprocess_token(token)
                            for token in complete_doc if is_token_allowed(token)]
print(complete_filtered_tokens)

# Rule-based matching - jeden z kroków do wyciągania informacji z nieustrukturyzowanego tekstu
matcher = Matcher(nlp.vocab)


# Funkcja do wyciągania imienia i nazwiska z tekstu
def extract_full_name(nlp_doc):
    pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
    matcher.add('FULL_NAME', None, pattern)
    matches = matcher(nlp_doc)
    for match_id, start, end in matches:
        span = nlp_doc[start:end]
        return span.text


extract_full_name(about_doc)

piano_text = 'Bartek uczy się grać na gitarze'
piano_doc = nlp(piano_text)
for token in piano_doc:
    print(token.text, token.tag_, token.head.text, token.dep_)

one_line_about_text = ('Gus Proto is a Python developer'
                       ' currently working for a London-based Fintech company')
one_line_about_doc = nlp(one_line_about_text)

# Extract children of `developer`
print([token.text for token in one_line_about_doc[5].children])

# Extract previous neighboring node of `developer`
print(one_line_about_doc[5].nbor(-1))

# Extract next neighboring node of `developer`
print(one_line_about_doc[5].nbor())

# Extract all tokens on the left of `developer`
print([token.text for token in one_line_about_doc[5].lefts])

# Extract tokens on the right of `developer`
print([token.text for token in one_line_about_doc[5].rights])

# Print subtree of `developer`
print(list(one_line_about_doc[5].subtree))

conference_text = ('Widziałem wczoraj ładny rower'
                   ' u mojego kolegi w garażu.')
conference_doc = nlp(conference_text)
# Extract Noun Phrases
for chunk in conference_doc.noun_chunks:
    print(chunk)

about_talk_text = ('The talk will introduce reader about Use'
                   ' cases of Natural Language Processing in'
                   ' Fintech')
pattern = r'(<VERB>?<ADV>*<VERB>+)'
about_talk_doc = textacy.make_spacy_doc(about_talk_text,
                                        lang='en_core_web_sm')
verb_phrases = textacy.extract.pos_regex_matches(about_talk_doc, pattern)
# Print all Verb Phrase
for chunk in verb_phrases:
    print(chunk.text)


# Extract Noun Phrase to explain what nouns are involved
for chunk in about_talk_doc.noun_chunks:
    print (chunk)

piano_class_text = ('Great Piano Academy is situated'
    ' in Mayfair or the City of London and has'
    ' world-class piano instructors.')
piano_class_doc = nlp(piano_class_text)
for ent in piano_class_doc.ents:
    print(ent.text, ent.start_char, ent.end_char,
          ent.label_, spacy.explain(ent.label_))

survey_text = ('Out of 5 people surveyed, James Robert,'
               ' Julie Fuller and Benjamin Brooks like'
               ' apples. Kelly Cox and Matthew Evans'
               ' like oranges.')

def replace_person_names(token):
    if token.ent_iob != 0 and token.ent_type_ == 'PERSON':
        return '[REDACTED] '
    return token.string

def redact_names(nlp_doc):
    for ent in nlp_doc.ents:
        ent.merge()
    tokens = map(replace_person_names, nlp_doc)
    return ''.join(tokens)

survey_doc = nlp(survey_text)
redact_names(survey_doc)
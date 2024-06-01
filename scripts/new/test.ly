\version "2.24.1"
\include "deutsch.ly"
jazzChords = { \semiGermanChords }
aFourL = {}
%\include "../config/include.ily"
markMoj = #(define-music-function (letter) (string?) #{ \mark \markup { \box \bold #letter } #})

\layout {
  indent = 0
}

\header {
  titlex = "Pjevajte Jahvi"
  title = "BLAGOSLIVLJAJ BOGA"
  composer = "F. Bosch / P. Horvat"
  %poet = "Women"
  style = "Women"
  broj = "1"
  %tagline = \markup { \override #'(font-name . "JohnSans White Pro") \override #'(font-size . -3) { Izvorno: Name, Album } }
}

\paper {
  \aFourL
  %min-systems-per-page = #7
  %annotate-spacing = ##t
  %system-system-spacing.padding = #3.2
  %page-breaking = #ly:one-page-breaking
  %last-bottom-spacing.minimum-distance = #8
}

staffOne = \relative c' {
  \key f \major
  \time 4/4
  \clef treble r8 a'8 g8 a4 g8 g8 f8 ~|
  f8 ~f4. a4 b8 a8 (|
  g4 )f4. ~f4 a8 |
  a4. c8 c8 b8 a4 |
  g8 r8 f8 e8 d4 f8 f8 |
  g4 g2. |
  r8 a8 g8 a4 g8 g8 f8 ~|
  f8 ~f4. a4 b8 a8 (|
  g4 )f2. |
  a4. c4 b8 a8 g8 |
  f8 r8 f8 e8 d4 f8 r8 |
  f8 e8 f2. |
  r8 b8 b8 b8 a8 g8 ~g4 ~|
  g8 r4 c,8 a'4 b8 a8 |
  g8 f8 ~f2. |
  r8 b8 b8 b8 a8 g8 ~g4 ~|
  g8 r4 c,8 a'4 b8 a8 |
  g8 f8 f2. |
  r4 r8 g8 g8 f8 f8 e8 |
  e8 ~e4. r4 r8 a8 |
  g8 g8 g8 f4 r4 r8 |
  r4 r8 g8 g8 g16 f16 f8 e8 ~|
  e8 ~e4. r4 c8 a'8 |
  g8 f8 f2. |
  r4 r8 a8 a8 g8 g8 f8 |
  f8 ~f4. r4 r8 a8 ~|
  a8 g8 f4. r4 f8 |
  g4 g8 r8 g8 g8 g8 g8 ~|
  g8 r8 a8 b8 g2 ~|
  g4 r2 r4 \bar "|." |
}

harmonyOne = \chordmode  {
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  s1 |
  \bar "|."
}

alignerOneZero = \relative {
  r8 c8 c8 c4 c8 c8 c8 |
  r8 r4. c4 c8 c8 |
  r4 c4. r4 c8 |
  c4. c8 c8 c8 c4 |
  c8 r8 c8 c8 c4 c8 c8 |
  c4 c2. |
  r8 c8 c8 c4 c8 c8 c8 |
  r8 r4. c4 c8 c8 |
  r4 c2. |
  c4. c4 c8 c8 c8 |
  c8 r8 c8 c8 c4 c8 r8 |
  c8 c8 c2. |
  r8 c8 c8 c8 c8 c8 r4 |
  r8 r4 c8 c4 c8 c8 |
  c8 r8 r2. |
  r8 c8 c8 c8 c8 c8 r4 |
  r8 r4 c8 c4 c8 c8 |
  c8 r8 c2. |
  r4 r8 c8 c8 c8 c8 c8 |
  c8 r4. r4 r8 c8 |
  r8 c8 c8 c4 r4 r8 |
  r4 r8 c8 c8 c16 c16 c8 c8 |
  r8 r4. r4 c8 c8 |
  r8 c8 c2. |
  r4 r8 c8 c8 c8 c8 c8 |
  c8 r4. r4 r8 c8 |
  r8 r8 c4. r4 c8 |
  c4 c8 r8 c8 c8 c8 c8 |
  r8 r8 c8 c8 c2 |
  r4 r2 r4 |
}

lyricOneZero = \lyricmode {
  Bla -- go -- sli -- vljaj Bo -- ga, -- %|
  du -- šo mo -- %|
  ja, -- i %|
  sve što je u me -- %|
  ni sve -- to i -- me nje -- %|
  go -- vo! %|
  Bla -- go -- sli -- vljaj Bo -- ga, -- %|
  du -- šo mo -- %|
  ja %|
  i ne za -- bo -- ra -- %|
  vi do -- bro -- čin -- stva %|
  nje -- go -- va: %|
  On ti ot -- pu -- šta %|
  sve grije -- he tvo -- %|
  je. -- %|
  On i -- scje -- lju -- je -- %|
  sve sla -- bo -- sti %|
  tvo -- je. %|
  On ti od pro -- pa -- %|
  sti -- ču -- %|
  va ži -- vot. %|
  Kru -- ni te do -- bro -- tom -- %|
  i lju -- %|
  bav -- lju. %|
  Ži -- vot ti i -- spu -- %|
  nja do -- %|
  brim. K'o %|
  or -- lu ti se mla -- dost %|
  ob -- nav -- lja. %|
  %|
}

\score {
    <<
    \new ChordNames { \jazzChords \harmonyOne }
    \new Staff {
        <<
        \new Voice { \staffOne }
        \new NullVoice = "alignerOneZero" { \alignerOneZero }
        \new Lyrics \lyricsto "alignerOneZero" { \lyricOneZero }
        >>
    }
    >>
}

\markup {
  \column {
  }
  \hspace #1
  \column {
  }
}

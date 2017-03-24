Shoshana and I fixed a grammar issue in FreeBSD's documentation Chapter 7.1 Multimedia Synopsis. 
We changed some incorret uses of playback to play back. Here is a link to our bug request: 
https://bugs.freebsd.org/bugzilla/show_bug.cgi?id=218073.



Here is our diff file:

  Index: chapter.xml
  ===================================================================
  --- chapter.xml	(revision 50082)
  +++ chapter.xml	(working copy)
  @@ -27,7 +27,7 @@

       <para>&os; supports a wide variety of sound cards, allowing users
         to enjoy high fidelity output from a &os; system.  This includes
  -      the ability to record and playback audio in the MPEG Audio Layer
  +      the ability to record and play back audio in the MPEG Audio Layer
         3 (<acronym>MP3</acronym>), Waveform Audio File
         (<acronym>WAV</acronym>), Ogg Vorbis, and other formats.  The
         &os; Ports Collection contains many applications for editing



Good documentation is the most important part of writing code. Without good documentation people
are not going to be able to understand how to use/maintain your project, and if no one can use your
project it's essentially useless. Good documentation allows users and developers alike to get 
software running correctly and quickly, reduces frustration, gets new users excited for the software, 
and enhances programming effort.

What I learned from this lab is the importance of good documentation. Also I learned how tetious 
documentation can be, and encouraged me to improve the documentation of my projects.

In search of the perfect blogging platform
##########################################

:date: 2014-07-23
:tags: musings, misc
:category: Random
:authors: Kushagra Sinha


What makes a good blogging platform?

Leaving the tech details, feature lists and other bells and whistles
aside, a good blogging platform's primary aim is twofold:

1. Make blogging enjoyable. Entice the blogger into writing more articles.
2. Make reading enjoyable. The output of the blogging platform should be easy
   to consume. A good support for themes and customizations is a must.

I had been using `Syte <https://github.com/rigoneri/syte>`_ as my hompage.
`Tumblr <https://www.tumblr.com/>`_ was the underlying blogging platform and
the whole thing was hosted on `Heroku <https://www.heroku.com/>`_. As it turns
out, all three of my aforementioned choices were suboptimal as far as my
blogging requirements were considered.

1. Syte was difficult to configure. I am neither a designer nor a front-end
   developer. Therefore it just lay stagnant, with the default theme.
2. Tumblr was not a good choice for a tech blog. Writing and highlighting code
   snippets is painful. Especially with a language like python, which uses
   indentation for denoting scope and one incorrect word-wrap in your theme
   can ruin the snippet. As it turns out, I churned out exactly two articles
   during my time on Tumblr. It is a great platform for other things, not for a
   tech blog in my humble opinion.
3. Though Heroku takes a lot of pain out of hosting your blog, it is far from
   ideal. I had to shift my site because I received a dreaded *Application Error*
   from Heroku. I had not looked into my site for a *very* long time and did
   not want to investigate.

A culmination of these problems forced me to look for alternatives. Thankfully,
I stumbled on `GitHub Pages <https://pages.github.com/>`_. I cannot recommend
them more. The setup is absolutely simple and your blog/site can be up and
running in no time.

However, I faced a few problems with `Jekyll <http://jekyllrb.com/>`_. Since,
it is based on Ruby, its installation was a nightmare for me due to the myriad
dependency management issues in Ruby. I naively tried
`Octopress <http://octopress.org/>`_ but later came to know that it was based
on Jekyll. (As a side, the dependency hell was primarily due to
`Bundler API outages <http://bundler.io/blog/2014/07/16/bundler-api-outages.html>`_).

By this time, I had become really interested in the idea of static site
generators. Being a python fan, I searched for a python based solution and
found `Pelican <http://blog.getpelican.com/>`_. It is fast, has good support
for themes and integrates with GitHub Pages with minimal effort from one's side.

The results of half a day of hacking is this blog.

Thanks for reading. Comments are welcome.

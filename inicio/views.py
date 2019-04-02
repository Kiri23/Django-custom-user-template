from django.shortcuts import render
import logging


# Create your views here.


def inicio(request):
    # Aunque le este enviando el context al index.html. El context puede viajar anidamente los template. index.html -> base.html -> navbar.hmtl
    context = {"indexNavActiveClass": "active"}
    logger = logging.getLogger("myproject")
    var = " my variable"
    # A string with a variable at the "info" level
    # logger.info("The value of var is %s", var)
    # logger.warning("Your log message is here. part 2")
    # logger.error('Something went wrong! testing 4 - views')

    return render(request, 'inicio/inicio.html', context)

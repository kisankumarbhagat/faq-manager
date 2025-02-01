from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from faq_app.models import FAQ
from faq_app.serializers import FAQSerializer
from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# View for rendering FAQ list in HTML
def faq_list(request):
    faqs = FAQ.objects.all()
    return render(request, 'faq_app/faq_list.html', {'faqs': faqs})

# API ViewSet for handling FAQ data (using Django REST Framework)
class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        lang = request.query_params.get('lang', 'en')  # Get language parameter (default 'en')
        cache_key = f'faqs_{lang}'  # Use cache key specific to the language
        
        # Check if FAQs are cached for the requested language
        faqs_data = cache.get(cache_key)
        
        if not faqs_data:
            faqs = FAQ.objects.all()  # Fetch all FAQ data from the database
            faqs_data = []
            for faq in faqs:
                translated_question = faq.get_translated_question(lang)  # Translate question based on lang
                faqs_data.append({
                    'question': translated_question,
                    'answer': faq.answer
                })
            
            # Cache the FAQ data for 15 minutes (900 seconds)
            cache.set(cache_key, faqs_data, timeout=60*15)
        
        return Response(faqs_data)

# Signal to clear cache when FAQ data is updated
@receiver(post_save, sender=FAQ)
@receiver(post_delete, sender=FAQ)
def clear_faq_cache(sender, **kwargs):
    cache.delete_pattern('faqs_*')  # Clears all cached FAQ data

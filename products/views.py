from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import UserSearchID
from .tasks import my_background_task



class ScrapperView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        content = {
            'user': str(request.user),
            'auth': str(request.auth), 
        }        
        return Response(content)

    def post(self, request):
        word = request.data.get('word')      
        sources = request.data.get('sources') 
        
        state = f"{request.user.state}"
        country = f"{request.user.country}"        
        location =   f"{state} , {country}"
        user = request.user
                        
        
        search_id_model = UserSearchID.objects.create(user=user, searched_word=word, searched_sources=sources)
        # kwargs = { "sources": sources, "word":word }       
        
        search_id = search_id_model.search_id
        timestamp = search_id_model.timestamp

        my_background_task.delay(search_id, **word)
                 
        if search_id:
            pass

      
            return Response({
                "status": "success", 
                "searched_word": word,
                "search_id": search_id,
                "timestamp": timestamp,
                "user": request.user.id,                                      
                }, 

                status=status.HTTP_200_OK)
        else:
            return Response({
                "status": "error",                 
                }, 
                status=status.HTTP_400_BAD_REQUEST)



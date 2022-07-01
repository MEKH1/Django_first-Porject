from sys import api_version
from urllib import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Room
from base.api.serializers import RoomSerialiazer
@api_view(['GET'])
def getRoutes(request):
    routes = [ 
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id',
    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerialiazer(rooms, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getRoom(request,pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerialiazer(room, many=False)
    return Response(serializer.data)


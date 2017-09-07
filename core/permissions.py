from rest_framework import permissions

from core.models import Profissional, Escritorio


class IsUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj == request.user


class IsProfissionalOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.user == request.user


class IsItemAgendaOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.profissional.user == request.user


class IsEscritorioOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            profissionais = Profissional.objects.filter(escritorio=obj)
            for profissional in profissionais:
                if profissional.user == request.user:
                    return True
            return False


class IsSalaOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            profissionais = Profissional.objects.filter(escritorio=obj.escritorio)
            for profissional in profissionais:
                if profissional.user == request.user:
                    return True
            return False
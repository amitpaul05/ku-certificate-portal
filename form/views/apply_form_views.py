from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from hall.models import Provost
from discipline.models import Head
from dsa.models import Dsa
from form.models import ApplyForm
from form.serializers.apply_form_serializers import ApplyFormSerializer, HeadApproveSerializer, LibrarianApproveSerializer, DsaApproveSerializer, ProvostApproveSerializer



class ApplyFormListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = ApplyFormSerializer

    def get_queryset(self):
        user = self.request.user

        if user.user_type == "student":
            return ApplyForm.objects.filter(student__user=user)

        elif user.user_type == "teacher":
            teacher = user.teachers

            # Head
            head_obj = Head.objects.filter(teacher=teacher).first()
            if head_obj:
                return ApplyForm.objects.filter(
                    student__discipline=head_obj.discipline,
                    is_head_approved=False,
                )

            # DSA
            dsa_obj = Dsa.objects.filter(teacher=teacher).first()
            if dsa_obj:
                return ApplyForm.objects.all(is_dsa_approved=False)

            # Provost
            provost_obj = Provost.objects.filter(teacher=teacher).first()
            if provost_obj:
                return ApplyForm.objects.filter(
                    hall=provost_obj.hall,
                    is_provost_approved=False
                )

        elif user.user_type == "librarian":
            return ApplyForm.objects.filter(is_librarian_approved=False)

        return ApplyForm.objects.none()



class HeadFormRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ApplyForm.objects.all()
    serializer_class = HeadApproveSerializer
    permission_classes = [IsAuthenticated,]
    lookup_field = 'id'


class DsaFormRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ApplyForm.objects.all()
    serializer_class = DsaApproveSerializer
    permission_classes = [IsAuthenticated,]
    lookup_field = 'id'


class LibrarianFormRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ApplyForm.objects.all()
    serializer_class = LibrarianApproveSerializer
    permission_classes = [IsAuthenticated,]
    lookup_field = 'id'


class ProvostFormRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = ApplyForm.objects.all()
    serializer_class = ProvostApproveSerializer
    permission_classes = [IsAuthenticated,]
    lookup_field = 'id'
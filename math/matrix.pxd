from . vector cimport Vector3
from . euler cimport Euler3

cdef struct Matrix4:
    float a11, a12, a13, a14
    float a21, a22, a23, a24
    float a31, a32, a33, a34
    float a41, a42, a43, a44

cdef struct Matrix3:
    float a11, a12, a13
    float a21, a22, a23
    float a31, a32, a33

ctypedef fused Matrix3_or_Matrix4:
    Matrix3
    Matrix4

cdef void transformVec3AsPoint_InPlace(Vector3* vector, Matrix4* matrix) nogil
cdef void transformVec3AsPoint(Vector3* target, Vector3* vector, Matrix4* matrix) nogil

cdef void transformVec3AsDirection_InPlace(Vector3* v, Matrix4* m) nogil
cdef void transformVec3AsDirection(Vector3* target, Vector3* v, Matrix4* m) nogil

cdef void setIdentityMatrix(Matrix3_or_Matrix4* m) nogil
cdef void setTranslationMatrix(Matrix4* m, Vector3* v) nogil
cdef void setRotationMatrix(Matrix3_or_Matrix4* m, Euler3* e) nogil
cdef void setScaleMatrix(Matrix3_or_Matrix4* m, Vector3* s) nogil

cdef void setTranslationScaleMatrix(Matrix4* m, Vector3* t, Vector3* s) nogil
cdef void setRotationScaleMatrix(Matrix3_or_Matrix4* m, Euler3* e, Vector3* s) nogil
cdef void setTranslationRotationScaleMatrix(Matrix4* m, Vector3* t, Euler3* e, Vector3* s) nogil

cdef void convertMatrix3ToMatrix4(Matrix4* t, Matrix3* s) nogil
cdef void convertMatrix4ToMatrix3(Matrix3* t, Matrix4* s) nogil

cdef void multMatrix3(Matrix3_or_Matrix4* target, Matrix3_or_Matrix4* x, Matrix3_or_Matrix4* y) nogil
cdef void multMatrix4(Matrix4* target, Matrix4* x, Matrix4* y) nogil
cdef void multMatrix3Parts(Matrix4* target, Matrix4* x, Matrix4* y, bint keepFirst = ?) nogil

from sorting import _merged, merge_sorted, quick_sorted, cmp_standard, cmp_reverse
from hypothesis import given
import hypothesis.strategies as st
import timeit


ints = st.lists(st.integers())


@given(str1=ints,str2=ints)
def test___merged(str1, str2):
    str1_sorted=sorted(str1)
    str2_sorted=sorted(str2)
    str12_sorted=sorted(str1+str2)
    assert _merged(str1_sorted,str2_sorted) == str12_sorted

@given(str1=ints,str2=ints)
def test___merged_cmp1(str1, str2):
    str1_sorted=list(reversed(sorted(str1)))
    str2_sorted=list(reversed(sorted(str2)))
    str12_sorted=list(reversed(sorted(str1+str2)))
    assert _merged(str1_sorted,str2_sorted,cmp=cmp_reverse) == str12_sorted

@given(str1=ints)
def test__merge_sorted(str1):
    assert merge_sorted(list(str1)) == sorted(str1)

@given(str1=ints)
def test__merge_sorted_cmp1(str1):
    assert merge_sorted(list(str1),cmp_reverse) == list(reversed(sorted(str1)))

@given(str1=ints)
def test__quick_sorted(str1):
    assert quick_sorted(list(str1)) == sorted(str1)

@given(str1=ints)
def test__quick_sorted_cmp1(str1):
    assert quick_sorted(list(str1),cmp_reverse) == list(reversed(sorted(str1)))

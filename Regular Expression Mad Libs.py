import re

text1 = """Giraffes have aroused
    the curiosity of __PLURAL_NOUN__
    since earliest times. The
    giraffe is the tallest of all
    living __PLURAL_NOUN__, but
    scientist are unable to
    explain how it got its long
    __PART_OF_THE_BODY__. The
    giraffe's tremendous height,
    which might reach __NUMBER__
    __PLURAL_NOUN__, comes from
    it legs and __BODYPART__.
    """

text2 = """I enjoy long __PLURAL_NOUN__
    in the park, and I love meeting up
    with __PLURAL_NOUN__ for drinks after
    work. In my spare time, I like to go
    __VERB_ENDING_WITH_ING__, especially
    if the weather is __ADJECTIVE__.
    Currently, my favorite yoga pose is
    __ANIMAL__, but I find it really
    challenging to accomplish if I've
    been drinking __TYPE_OF_FLUID__.
    Currently, I'm reading a book about
    __VERB_ENDING_WITH_ING__, which has
    proven to be very __ADJECTIVE__. My
    favorite band is the __VERB_ENDING_WITH_ING__
    __ANIMAL_PLURAL__, which I listened to
    while I was __VERB_ENDING_WITH_ING__ my
    way to work.
    """


def mad_libs(mls):
    """
    :param mls: String
    with parts the user
    should fill out surrounded
    by double underscores.
    Underscores cannot
    be inside hint e.g., no
    __hint_hint__ only
    __hint__.
    """
    hints = re.findall("__.*?__",
                       mls)
    if hints is not None:
        for word in hints:
            q = "Enter a {}".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
        print ('\n')
        mls = mls.replace("\n", " ")
        print(mls)
    else:
        print("invalid mls")

mad_libs(text1)
mad_libs(text2)

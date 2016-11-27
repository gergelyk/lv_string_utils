_CITE = '<cite>' 
CITE_ = '</cite>'
_CCITE = '<code class="docutils literal"><span class="pre">'
CCITE_ = '</span></code>'

cts_basic_text = r"""
double            | 123.000000                      | Input of the VI is a {_CITE}Variant{CITE_}. Whatever you connect to this input must be casted explicitely...
double_auto       | 123.000000                      | ...or implicitely.
fxp               | 3.750000                        | VI uses default formatting for all numerical data types. Data types with units are not supported.
boolean           | True                            | Boolean values are represented by {_CCITE}False{CCITE_} and {_CCITE}True{CCITE_} keywords known from Python and not {_CCITE}FALSE{CCITE_} and {_CCITE}TRUE{CCITE_} as it can be observed in LabVIEW.
enum_name         | Second                          | In case of enums, VI shows names of the constants...<br><img src="_static/img/format/enum_values.png">
enum_value        | 1                               | ...of course, unless you cast enum to numerical type.
class             | LabVIEW Object                  | Objects are represented by names of their classes.
reference         | 0x4A000031                      | References are shown as memory locations (32-bit hexadecimal addresses) which they correspond to.
string            | 'abc\ndef'                      | Special characters in the strings are escaped. Quotation marks are added. This conforms behaviour of {_CCITE}repr{CCITE_} function in Python.
path              | 'C:\'                           | Paths as considered the same way as strings.
timestamp         | 1904-01-01 12:00:00.000000      | Following default formatting string is applied to timestamps: <pre>%^<%Y-%m-%d %H:%M:%S%06u>T</pre> More details can be found <a href="http://zone.ni.com/reference/en-XX/help/371361H-01/glang/codes_for_time_format_str/">here</a>.
variant           | <i>non-printable</i>            | {_CITE}Variants{CITE_} are flattened to strings the same way as LabVIEW built-in function {_CCITE}Variant To Flattened String{CCITE_} would do.
variant_dbl       | <i>non-printable</i>            | Double occurence of {_CCITE}To Variant{CCITE_} function can be substituted by <a href="to_nested_variant.html">To Nested Variant.vi</a>.
array_simple      | [[1, 2, 3], [6, 7, 8]]          | Arrays are displayed row by row, the same way as nested lists in Python.
cluster_named     | {{'foo': 123, 'bar': False}}    | Cluster, elements of which have <u>non-empty</u> labels is printed as a {_CITE}dictionary{CITE_} in Python.
cluster_unnamed   | {{123, False}}                  | Cluster, elements of which have <u>empty</u> labels is printed as a {_CITE}set{CITE_} in Python.
waveform          | [0.000000, 0.062791, 0.125333,<br>...<br>-0.187381, -0.125333, -0.062791]              | In case of {_CITE}Waveforms{CITE_}, only data is converted to string. The same applies to {_CITE}Digital Waveforms{CITE_} and {_CITE}Digital Data{CITE_} types.<br>Note that three dots on the left denote part of the string which hasn't been presented here, but is returned by the VI.
"""

cts_adv_text = r"""
array_var         | [True, [[1, 2, 3], [6, 7, 8]]]  | Heterogeneous arrays are supported too. Each element of such array must be a {_CITE}Variant{CITE_}.
cluster_nested    | {{8.000000, {{'status': True, 'code': -1, 'source': 'Error'}}, [False, True, False]}}  | Nested clusters correspond to nested {_CITE}dictionaries{CITE_} and {_CITE}sets{CITE_} in Python. Note that labels of the elements can be hidden, but will still appear in the string if they are non-empty.
"""

fc_basic_text = r"""
implicite_variant      | 1.230000        | <b>Implicite default formatting.</b><br>Built-in type, scalar. Data casted to {_CITE}Variant{CITE_} manually.
implicite              | 1.230000        | <b>Implicite default formatting.</b><br>Built-in type, scalar. Data casted to {_CITE}Variant{CITE_} automatically.
default                | 1.230000        | <b>Implicite custom formatting.</b><br>Built-in type, scalar. Note that data has ben casted to {_CITE}Variant{CITE_} twice.
default_short          | 1.230000        | <b>Implicite custom formatting.</b><br>Built-in type, scalar. The same as above, but double casting has been performed by <a href="to_nested_variant.html">To Nested Variant.vi</a>.
custom                 | Value: 1.230000 | <b>Explicite formatting</b>.<br>Built-in type, scalar. Simple case.
custom_adv             | Value: 1.230    | <b>Explicite formatting.</b><br>Built-in type, scalar. A bit more advanced than above.
default_obj            | LabVIEW Object  | <b>Implicite custom formatting.</b><br>Instance of the class.
default_arr            | [[1.000000, 2.000000, 3.000000], [6.000000, 7.000000, 8.000000]] | <b>Implicite default formatting.</b><br>Array.
"""

fc_special_text = r"""
bool_native_dec        | 1                    | Natively, LabVIEW can convert boolean values as they were decimal...
bool_native_str        | TRUE                 | ...or as they were stirngs. This returns names of the values in upper case though.
bool_native_def        | True                 | If we want to be Python-compatible, we need CamelCase. This can be achieved by using <b>implicite custom formatting</b>.
enum_str               | second               | Enums can be converted by using names of the constants... <img src="_static/img/format/enum_values.png">
enum_dec               | 1                    | ...or by using values of the constants.
enum_str_dec           | Value of second is 1 | The same constant is dispayed twice. Once as a name and then as a value.
string                 | abc<br>def           | {_CCITE}s{CCITE_} placeholder is the one which natively goes together with string data type. This is why it returns input data as it is. This case can be clasified as <b>explicite formatting</b>.
string_variant         | 'abc\ndef'           | If we want to be compatible wiht Python {_CCITE}repr{CCITE_} function, string data type needs to be provided in a variant. This results in <b>implicite custom formatting</b>.
variant                | <i>non-printable</i> | In cases when we need {_CITE}Variant{CITE_} type to be flattened into string, triple casting is necessary.
"""

fc_cont_text = r"""
arr_dec                | [1, 2, 3]                   | <b>Implicite defaut formatting</b> of homogenous array.
arr_dec_form           | 1..2..3..                   | <b>Element-wise explicite formatting</b> of homogenous array. Note that spare placeholders have been discarded.
arr_dec_var            | Data is: [1, 2, 3]          | <b>Implicite custom formatting</b> of homogenous array with a string preceding data.
arr_var_expl           | 1; 123.000                  | <b>Element-wise explicite formatting</b> of heterogeneous array. Note that each element has been manually casted to {_CITE}Variant{CITE_}.
arr_var_impl           | 1; 123.000                  | The same as above, but only the first element has been casted to {_CITE}Variant{CITE_} manually. Remaining elements can be casted automatically.
arr_nest               | [True, 123.000000, 1, 2, 3] | <b>Implicite defaut formatting</b> of heterogeneous array. Note that {_CCITE}Build Array{CCITE_} function concatenates inputs. Elements of input array are one by one casted to {_CITE}Variants{CITE_}.
arr_nest_form          | 1; 123.000; 1-2-3           | <b>Element-wise explicite formatting</b> of heterogeneous array. Note that {_CCITE}Build Array{CCITE_} function concatenates inputs. Elements of input array are one by one casted to {_CITE}Variants{CITE_}.
arr_nest_var           | 1; 123.000; [1, 2, 3]       | <b>Element-wise mixed formatting</b> of heterogeneous array. Input array has been casted to {_CITE}Variants{CITE_} twice, which makes {_CCITE}Build Array{CCITE_} function consider it as a single element. First two elements of resulting array have been formated <b>explicitely</b>. The last element has been formated using <b>implicite custom formatting</b>.
clust_wrong            | <i>unspecified</i>          | In contrast to arrays which can be concatenated, clusters cannot be linearized. This means that clusters that contain other containers cannot be formatted element-wise...
clust                  | 1; 123.000; [1, 2, 3]       | ...until containers are casted to {_CITE}Variant{CITE_} type for further <b>implicite custom formatting</b>.
clust_const            | 1; 123.000; [1, 2, 3]       | Naturally, the same data as above can be placed in code as a constant, without using {_CCITE}Bundle{CCITE_} function.
"""

def full_text_to_list(text, loc):
    return [[col.strip() for col in row.strip().split('|')] for row in text.strip().format(**loc).splitlines()]

loc = locals()
cts_basic  = full_text_to_list(cts_basic_text, loc)
cts_adv    = full_text_to_list(cts_adv_text, loc)
fc_basic   = full_text_to_list(fc_basic_text, loc)
fc_special = full_text_to_list(fc_special_text, loc)
fc_cont    = full_text_to_list(fc_cont_text, loc)





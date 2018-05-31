import ipywidgets as ipw

template = """
<table>
<tr>
  <th style="text-align:center">Persistence Homology</th>
<tr>
  <td valign="top"><ul>
    <li><a href="{appbase}/barcode.ipynb" target="_blank">Compute barcode</a></li>
  </ul></td>
</tr>
</table>
"""


def get_start_widget(appbase, jupbase, notebase):
    html = template.format(appbase=appbase, jupbase=jupbase, notebase=notebase)
    return ipw.HTML(html)


#EOF

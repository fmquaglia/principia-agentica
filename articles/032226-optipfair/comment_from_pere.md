Fabricio! Le he dado un vistazo! Muchisimas gracias!

Te comento un par de cosas, no es que esten mal, es que optipfair va evolucionando rapido. Sabes cuando dices que width pruning rompe la estreuctura? En un principio lo he solucionado, ahora puedes indicar un expansioon_divisor para respetar tamaño de tensor cores: Se puede indicar 32, 64, 128 y 256. Al realizar el width pruning respeta que sea divisible.

```python
pruned_model_optip, stats = prune_model(
    model=model,
    pruning_type="MLP_GLU",
    neuron_selection_method="MAW",
    pruning_percentage=40,
    expansion_divisor=64,
    dataloader=dataloaderwiki,
    show_progress=True,
    return_stats=True
)
```
En el codigo de arriba ves dos parametros nuevos (creo que no estaban).
* expansion_divisor
* data_loader. Si le pasas un data loader, width pruning como en depth pruning optipfair calcula, que neurones o bloques transformer aportan menos al trabajar con ese dataloader y son los que elimina.

Te paso una imagen de como funciona el método data-driven en width pruning, por que realmente creo que es casi unico, esta basado en un paper que se llama CFSP, pero muy modificado y simplificado.

Un abrazo!
Lo de la futura serie de optipfair, cuando quieras Fabricio, yo voy añadiendo funcionalidades casi de forma continua.
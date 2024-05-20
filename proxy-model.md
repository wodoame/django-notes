In Django, a **proxy model** is a model that **inherits from an existing model**, but **does not have its own database table**. Instead, it **uses the database table of the model it inherits from**. Here are some key points about proxy models:

1. **Purpose**:
   - Proxy models are often used to **add or change the behavior** of the original model **without modifying its fields or database table**.
   - They provide an alternative interface to the same underlying data.

2. **Declaration**:
   - You declare a proxy model like a normal model, but you set the `proxy` attribute of the `Meta` class to `True`.
   - For example:
     ```python
     class MyProxyModel(MyOriginalModel):
         class Meta:
             proxy = True
     ```

3. **Use Cases**:
   - Customize query sets for specific use cases.
   - Change the ordering of results.
   - Annotate the model with a different name than the parent.
   - Extend the original model's functionality without altering its structure.

Remember that proxy models don't create a new database table; they simply provide a different way to interact with the existing data.

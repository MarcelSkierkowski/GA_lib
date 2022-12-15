schema = {
    "genes_size":
        {
            'type': 'list',
            'minlength': 1,
            'schema':
                {
                    'type': 'integer',
                    'min': 1
                }
        },

    "genes_range":
        {
            'type': 'list',
            'minlength': 1,
            'schema':
                {
                    'type': 'list',
                    'schema':
                        {
                            'type': 'float',
                            'maxlength': 2
                        }
                }
        },

    "mutation_probability":
        {
            'type': 'float',
            'min': 0,
            'max': 1
        }
}

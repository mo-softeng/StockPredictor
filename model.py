if __name__ == "__model__":
    from prepareData import x_train, y_train
    import tensorflow as tf
    # recurrent neural networks (rnns), good for predicting future values based on past sequeneces
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.LSTM(units=50, activation = 'relu', return_sequences = True, input_shape =(x_train.shape[1], 1)))
    model.add(tf.keras.layers.Dropout(0.2))

    model.add(tf.keras.layers.LSTM(units=60, activation = 'relu', return_sequences = True))
    model.add(tf.keras.layers.Dropout(0.3))

    model.add(tf.keras.layers.LSTM(units=80, activation = 'relu', return_sequences = True))
    model.add(tf.keras.layers.Dropout(0.4))

    model.add(tf.keras.layers.LSTM(units=120, activation = 'relu'))
    model.add(tf.keras.layers.Dropout(0.5))

    model.add(tf.keras.layers.Dense(units=1))


    model.compile(optimizer="adam", loss='mean_squared_error')
    model.fit(x_train, y_train, epochs = 10)
    model.save("keras_model.keras")
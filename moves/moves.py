import numpy as np


class Movement:
    def __init__(self):
        self.counter = 0
        self.state = None

    def get_counter(self):
        return self.counter

    def get_state(self):
        return self.state

    def get_label(self):
        return self.label


class BicepsLeft(Movement):  # print
    """
    Identifica o exercício físico do tipo "rosca bíceps"
    para o braço esquerdo.
    """

    def __init__(self):
        super().__init__()
        self.label = 'Flexao de biceps esquerdo'

    def update(self, shoulder_left, elbow_left, wrist_left):
        """
        Esta solução de cálculo de ângulo entre dois vetores encontra-se no
        StackOverflow:
        https://stackoverflow.com/questions/21483999/using-atan2-to-find-angle-between-two-vectors
        Somente aqui eu utilizo esta solução. Mais para frente, utilizo
        "a minha solução" que nada mais é do que a definição do produto
        interno entre dois vetores.
        """
        # Calculate angle
        shoulder_left = np.array(shoulder_left)
        elbow_left = np.array(elbow_left)
        wrist_left = np.array(wrist_left)

        radians = np.arctan2(wrist_left[1] - elbow_left[1], wrist_left[0] - elbow_left[0]) - \
            np.arctan2(shoulder_left[1] - elbow_left[1],
                       shoulder_left[0] - elbow_left[0])
        angle = np.abs(radians * 180.0 / np.pi)

        if angle > 180.0:
            angle = 360 - angle

        # Curl counter logic
        if angle > 160:
            self.state = "down"
        if angle < 30 and self.state == "down":
            self.state = "up"
            self.counter += 1


class BicepsRight(Movement):
    """
    Identifica o exercício físico do tipo "rosca bíceps"
    para o braço direito.
    """

    def __init__(self):
        super().__init__()
        self.label = 'Flexao de biceps direito'

    def update(self, shoulder_right, elbow_right, wrist_right):
        # Calculate angle
        shoulder_right = np.array(shoulder_right)  # First
        elbow_right = np.array(elbow_right)  # Mid
        wrist_right = np.array(wrist_right)  # End

        radians = np.arctan2(wrist_right[1] - elbow_right[1], wrist_right[0] - elbow_right[0]) - \
            np.arctan2(shoulder_right[1] - elbow_right[1],
                       shoulder_right[0] - elbow_right[0])
        angle = np.abs(radians * 180.0 / np.pi)

        if angle > 180.0:
            angle = 360 - angle

        # Curl counter logic
        if angle > 160:
            self.state = "down"
        if angle < 30 and self.state == "down":
            self.state = "up"
            self.counter += 1


class StretchedLeftArm(Movement):
    """
    Identifica quando o braço esquerdo está esticado horizontalmente,
    como se formasse 90° com o tronco e paralelo ao chão.
    """

    def __init__(self):
        super().__init__()
        self.label = 'Braco esquerdo esticado horizontalmente'

    def update(self, right_shoulder, left_shoulder, left_elbow, left_wrist):
        left_most_x = min(left_shoulder[0], left_elbow[0], left_wrist[0])
        right_most_x = max(left_shoulder[0], left_elbow[0], left_wrist[0])

        width_arms = right_most_x - left_most_x
        width_chest = abs(right_shoulder[0] - left_shoulder[0])

        if width_arms / width_chest > 1 and self.state == "down":
            self.state = "up"
            self.counter += 1
        if width_arms / width_chest <= 1:
            self.state = "down"


class StretchedRightArm(Movement):
    """
    Identifica quando o braço direito está esticado horizontalmente,
    como se formasse 90° com o tronco e paralelo ao chão.
    """

    def __init__(self):
        super().__init__()
        self.label = 'Braco direito esticado horizontalmente'

    def update(self, left_shoulder, right_shoulder, right_elbow, right_wrist):
        left_most_x = min(right_shoulder[0], right_elbow[0], right_wrist[0])
        right_most_x = max(right_shoulder[0], right_elbow[0], right_wrist[0])

        width_arms = right_most_x - left_most_x

        width_chest = abs(right_shoulder[0] - left_shoulder[0])

        if width_arms / width_chest > 1 and self.state == "down":
            self.state = "up"
            self.counter += 1
        if width_arms / width_chest <= 1:
            self.state = "down"


class RaisedLeftArm(Movement):
    """
    Identifica quando o braço esquerdo está esticado verticalmente
    para cima, como se paralelo ao tronco.
    """

    def __init__(self):
        super().__init__()
        self.label = 'Braco esquerdo esticado verticalmente'

    def update(self, left_hip, left_shoulder, left_elbow, left_wrist):
        lower_most_y = min(left_shoulder[1], left_elbow[1], left_wrist[1])
        top_most_y = max(left_shoulder[1], left_elbow[1], left_wrist[1])

        height_arms = abs(lower_most_y - top_most_y)
        height_torso = abs(left_hip[1] - left_shoulder[1])

        if height_arms / height_torso > 0.8 and left_wrist[1] < left_shoulder[1] and self.state == "down":
            self.state = "up"
            self.counter += 1

        if height_arms / height_torso <= 0.8 or left_wrist[1] > left_shoulder[1]:
            self.state = "down"


class RaisedRightArm(Movement):
    """
    Identifica quando o braço direito está esticado verticalmente
    para cima, como se paralelo ao tronco.
    """

    def __init__(self):
        super().__init__()
        self.label = 'Braco direito esticado verticalmente'

    def update(self, right_hip, right_shoulder, right_elbow, right_wrist):
        lower_most_y = min(right_shoulder[1], right_elbow[1], right_wrist[1])
        top_most_y = max(right_shoulder[1], right_elbow[1], right_wrist[1])

        height_arms = abs(lower_most_y - top_most_y)
        height_torso = abs(right_hip[1] - right_shoulder[1])

        if height_arms / height_torso > 0.8 and right_wrist[1] < right_shoulder[1] and self.state == "down":
            self.state = "up"
            self.counter += 1

        if height_arms / height_torso <= 0.8 or right_wrist[1] > right_shoulder[1]:
            self.state = "down"


class RestLeftArm(Movement):
    """
    Identifica quando o braço esquerdo está esticado verticalmente
    para baixo, como se paralelo ao tronco. Ou seja, identifica quando
    o braço esquerdo está "descansando".
    """

    def __init__(self):
        super().__init__()
        self.label = 'Braco esquerdo descansando'

    def update(self, left_hip, left_shoulder, left_elbow, left_wrist):
        lower_most_y = min(left_shoulder[1], left_elbow[1], left_wrist[1])
        top_most_y = max(left_shoulder[1], left_elbow[1], left_wrist[1])

        height_arms = abs(lower_most_y - top_most_y)
        height_torso = abs(left_hip[1] - left_shoulder[1])

        if height_arms / height_torso > 0.9 and left_wrist[1] > left_shoulder[1] and self.state == "down":
            self.state = "up"
            self.counter += 1

        if height_arms / height_torso <= 0.9 or left_wrist[1] < left_shoulder[1]:
            self.state = "down"


class RestRightArm(Movement):
    """
    Identifica quando o braço direito está esticado verticalmente
    para baixo, como se paralelo ao tronco. Ou seja, identifica quando
    o braço direito está "descansando".
    """

    def __init__(self):
        super().__init__()
        self.label = 'Braco direito descansando'

    def update(self, right_hip, right_shoulder, right_elbow, right_wrist):
        lower_most_y = min(right_shoulder[1], right_elbow[1], right_wrist[1])
        top_most_y = max(right_shoulder[1], right_elbow[1], right_wrist[1])

        height_arms = abs(lower_most_y - top_most_y)
        height_torso = abs(right_hip[1] - right_shoulder[1])

        if height_arms / height_torso > 0.9 and right_wrist[1] > right_shoulder[1] and self.state == "down":
            self.state = "up"
            self.counter += 1

        if height_arms / height_torso <= 0.9 or right_wrist[1] < right_shoulder[1]:
            self.state = "down"


class HandTouch(Movement):
    """
    Identifica quando as duas mãos se encostam.
    Verificar porque nãoe stá entradno no if com None e está contando infinito.
    """

    def __init__(self):
        super().__init__()
        self.label = 'Maos se encostam'

    def update(self, right_index, left_index):
        if (
            left_index[0] - 0.1*left_index[0]) <= right_index[0] <= (left_index[0] + 0.1*left_index[0]
                                                                     ) and (
                left_index[1] - 0.1*left_index[1]) <= right_index[1] <= (left_index[1] + 0.1*left_index[1]) and self.state == None:
            self.state = "up"
            self.counter += 1
        if (
            left_index[0] - 0.3*left_index[0]) <= right_index[0] <= (left_index[0] + 0.3*left_index[0]
                                                                     ) and (
                left_index[1] - 0.3*left_index[1]) <= right_index[1] <= (left_index[1] + 0.3*left_index[1]):
            self.state = None


class Raised(Movement):
    """
    A pessoa está em pé.
    """

    def __init__(self):
        super().__init__()
        self.label = 'Pessoa em pe'

    def update(self, right_shoulder, left_shoulder):
        if right_shoulder[1] < 0.2 and left_shoulder[1] < 0.2 and self.state == "down":
            self.state = "up"
            self.counter += 1

        if right_shoulder[1] >= 0.2 and left_shoulder[1] >= 0.2:
            self.state = "down"


class Lowered(Movement):
    """
    A pessoa está agachada.
    """

    def __init__(self):
        super().__init__()
        self.label = 'Pessoa agachada'

    def update(self, right_shoulder, left_shoulder):
        if right_shoulder[1] > 0.8 and left_shoulder[1] > 0.8 and self.state == "down":
            self.state = "up"
            self.counter += 1

        if right_shoulder[1] <= 0.8 and left_shoulder[1] <= 0.8:
            self.state = "down"


class StrongLeft(Movement):
    """
    Identifica o "ato de mostrar o muque" com braço esquerdo.
    """

    def __init__(self):
        super().__init__()
        self.label = 'Mostrando muque esquerdo'

    def update(self, vetor_1, vetor_2, origem=[0, 0]):
        u = [vetor_1[0] - origem[0], vetor_1[1] - origem[1]]
        v = [vetor_2[0] - origem[0], vetor_2[1] - origem[1]]

        u = np.array(u)
        v = np.array(v)
        modulo_u = np.sqrt(np.sum(u**2))
        modulo_v = np.sqrt(np.sum(v**2))
        produto_interno_u_v = np.inner(u, v)
        theta = np.arccos((produto_interno_u_v) / (modulo_u * modulo_v))
        # Transformando o ângulo de rad para graus
        theta = theta*57.2958

        if 105 <= theta or theta <= 75:
            self.state = "up"
        if 80 <= theta <= 100 and self.state == "up":
            self.state = None
            self.counter += 1


class StretchedLeftLeg(Movement):
    """
    Identifica o ato de levantar a perna esquerda lateralmente.
    """

    def __init__(self):
        super().__init__()
        self.label = 'Levantamento lateral perna esquerda'

    def update(self, vetor_1, vetor_2, origem=[0, 0]):
        u = [vetor_1[0] - origem[0], vetor_1[1] - origem[1]]
        v = [vetor_2[0] - origem[0], vetor_2[1] - origem[1]]

        u = np.array(u)
        v = np.array(v)
        modulo_u = np.sqrt(np.sum(u**2))
        modulo_v = np.sqrt(np.sum(v**2))
        produto_interno_u_v = np.inner(u, v)
        theta = np.arccos((produto_interno_u_v) / (modulo_u * modulo_v))
        # Transformando o ângulo de rad para graus
        theta = theta*57.2958

        if theta <= 120:
            self.state = "up"
        if theta > 120 and self.state == "up":
            self.state = None
            self.counter += 1


class StretchedRightLeg(Movement):
    """
    Identifica o ato de levantar a perna direita lateralmente.
    """

    def __init__(self):
        super().__init__()
        self.label = 'Levantamento lateral perna direita'

    def update(self, vetor_1, vetor_2, origem=[0, 0]):
        u = [vetor_1[0] - origem[0], vetor_1[1] - origem[1]]
        v = [vetor_2[0] - origem[0], vetor_2[1] - origem[1]]

        u = np.array(u)
        v = np.array(v)
        modulo_u = np.sqrt(np.sum(u**2))
        modulo_v = np.sqrt(np.sum(v**2))
        produto_interno_u_v = np.inner(u, v)
        theta = np.arccos((produto_interno_u_v) / (modulo_u * modulo_v))
        # Transformando o ângulo de rad para graus
        theta = theta*57.2958

        if theta <= 120:
            self.state = "up"
        if theta > 120 and self.state == "up":
            self.state = None
            self.counter += 1


class LeftHandMouth(Movement):
    """
    Identifica quando a mão esquerda é levada na boca.
    """

    def __init__(self):
        super().__init__()
        self.label = 'Mao esquerda na boca'

    def update(self, point_1, point_2):
        dif_x = point_1[0] - point_2[0]
        dif_y = point_1[1] - point_2[1]
        distance = np.sqrt((dif_x)**2 + (dif_y)**2)

        if distance <= 0.08 and self.state == None:
            self.state = "up"
            self.counter += 1
        if distance > 0.08 and self.state == "up":
            self.state = None


class RightHandMouth(Movement):
    """
    Identifica quando a mão direita é levada na boca.
    """

    def __init__(self):
        super().__init__()
        self.label = 'Mao direita na boca'

    def update(self, point_1, point_2):
        dif_x = point_1[0] - point_2[0]
        dif_y = point_1[1] - point_2[1]
        distance = np.sqrt((dif_x)**2 + (dif_y)**2)

        if distance <= 0.08 and self.state == None:
            self.state = "up"
            self.counter += 1
        if distance > 0.08 and self.state == "up":
            self.state = None


class Side(Movement):
    """
    Identifica quando a pessoa está de lado para a câmera.
    """

    def __init__(self):
        super().__init__()
        self.label = 'Virou de lado'

    def update(self, vetor_1, vetor_2, origem=[0, 0]):
        u = [vetor_1[0] - origem[0], vetor_1[1] - origem[1]]
        v = [vetor_2[0] - origem[0], vetor_2[1] - origem[1]]

        u = np.array(u)
        v = np.array(v)
        modulo_u = np.sqrt(np.sum(u**2))
        modulo_v = np.sqrt(np.sum(v**2))
        produto_interno_u_v = np.inner(u, v)
        theta = np.arccos((produto_interno_u_v) / (modulo_u * modulo_v))
        # Transformando o ângulo de rad para graus
        theta = theta*57.2958

        if theta > 4:
            self.state = "up"
        if theta <= 4 and self.state == "up":
            self.state = None
            self.counter += 1


class Rest(Movement):
    """
    Identifica quando a pessoa se deita.
    """

    def __init__(self):
        super().__init__()
        self.label = 'Deitou'

    def update(self, point_1, point_2):
        dif_y = abs(point_1[1] - point_2[1])

        if dif_y <= 0.1 and self.state == None:
            self.state = "up"
            self.counter += 1
        if dif_y > 0.1 and self.state == "up":
            self.state = None


class HeadToLeft(Movement):
    """
    Identifica quando a pessoa inclinou a cabeça para o lado esquerdo.
    """

    def __init__(self):
        super().__init__()
        self.label = 'Inclinou cabeca para a esquerdaa'

    def update(self, vetor_1, vetor_2, origem=[0, 0]):
        u = [vetor_1[0] - origem[0], vetor_1[1] - origem[1]]
        v = [vetor_2[0] - origem[0], vetor_2[1] - origem[1]]

        u = np.array(u)
        v = np.array(v)
        modulo_u = np.sqrt(np.sum(u**2))
        modulo_v = np.sqrt(np.sum(v**2))
        produto_interno_u_v = np.inner(u, v)
        theta = np.arccos((produto_interno_u_v) / (modulo_u * modulo_v))
        # Transformando o ângulo de rad para graus
        theta = theta*57.2958

        if theta > 10:
            self.state = "up"
        if theta <= 5 and self.state == "up":
            self.state = None
            self.counter += 1


class HeadToRight(Movement):
    """
    Identifica quando a pessoa inclinou a cabeça para o lado direito.
    """

    def __init__(self):
        super().__init__()
        self.label = 'Inclinou cabeca para a direita'

    def update(self, vetor_1, vetor_2, origem=[0, 0]):
        u = [vetor_1[0] - origem[0], vetor_1[1] - origem[1]]
        v = [vetor_2[0] - origem[0], vetor_2[1] - origem[1]]

        u = np.array(u)
        v = np.array(v)
        modulo_u = np.sqrt(np.sum(u**2))
        modulo_v = np.sqrt(np.sum(v**2))
        produto_interno_u_v = np.inner(u, v)
        theta = np.arccos((produto_interno_u_v) / (modulo_u * modulo_v))
        # Transformando o ângulo de rad para graus
        theta = theta*57.2958

        if theta > 10:
            self.state = "up"
        if theta <= 5 and self.state == "up":
            self.state = None
            self.counter += 1
